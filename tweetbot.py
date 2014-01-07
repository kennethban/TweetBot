'''
Tweetbot for regular posting of revision notes

Created 30 Sept 2013

@author: Kenneth Ban (kennethban@gmail.com)
'''

# import modules
# non-std library items: ConfigParser, twython

import os
import ConfigParser
import logging
import sqlite3
import random
from twython import Twython, TwythonError
from datetime import datetime

# define helper functions

def weighted_choice(d):
    for key in d:
        d[key] = int(d[key])
    r = random.uniform(0,sum(d.itervalues()))
    s = 0.0
    for k,w in d.iteritems():
        s+=w
        if r<s: return k
    return k

def weekday(day):
    days = {'mon':0,'tue':1,'wed':2,'thu':3,'fri':4,'sat':5,'sun':6}
    return days[day]

def tweetday(today,schedule_days):
    if today in schedule_days:
        return True
    else:
        return False

# main

# set directories, change to current working directory where all config/database/log files reside

os.chdir(os.path.dirname(__file__))

# enable logging

logging.basicConfig(filename='tweetbot.log',level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
logging.info('Started')

# get configuration details

config = ConfigParser.ConfigParser()

try:
    config.read("tweetbot.cfg")
except ConfigParser.Error:
    logging.critical('Could not parse configuration file')
    exit()

consumer_token = config.get('twitter','consumer_token')
consumer_secret = config.get('twitter','consumer_secret')
access_token = config.get('twitter','access_token')
access_secret = config.get('twitter','access_secret')

tweetdb = config.get('sqlite','tweetdb')
topic_priority = dict(config.items('topic'))
schedule_days = [ weekday(x.strip()) for x in config.get('schedule','days').split(',')]

# check if today is on schedule for tweeting

today = datetime.now().date().weekday()

if not tweetday(today,schedule_days):
    logging.info('Not scheduled day: %s',config.get('schedule','days'))
    exit()

# check twitter authentication first and abort if fails

twitter = Twython(consumer_token, consumer_secret, access_token, access_secret)

try:
    twitter.verify_credentials()
except TwythonError as e:
    logging.critical('Cannot authenticate with Twitter: %s',e)
    exit()

# get database

logging.info('Loading database')

try:
    con = sqlite3.connect(tweetdb)
except sqlite3.DatabaseError:
    logging.critical('Cannot load database')
        
current = con.cursor()

# check if any unposted notes
# if none left, reset counts in the database

current.execute("SELECT topic from NOTES where count=0")
records = current.fetchall()

if len(records) == 0:
    print "Resetting counts..."
    current.execute("UPDATE NOTES SET count=0")
    con.commit()
    current.execute("SELECT topic from NOTES where count=0")
    records = current.fetchall()

# get topics and select based on priority

topics = [x[0] for x in records]
topics_weighted = {k:topic_priority.get(k) for k in topics}
topic_choice = weighted_choice(topics_weighted)

# get ids within topic choice and choose randomly

current.execute("SELECT id from NOTES where topic=? AND count=0",(topic_choice,))
records = current.fetchall()

ids = [x[0] for x in records]
note_choice = random.choice(ids)

# get note,link for the selected id

current.execute("SELECT note,link from NOTES where id=?",(note_choice,))
record = current.fetchone()
note = record[0]
link = record[1]

if link:
    tweet = note + " " + link
else:
    tweet = note
    
# post tweet

try:
    twitter.update_status(status=tweet)
except TwythonError as e:
    logging.critical('Unable to post tweet: %s',e)
    exit()

logging.info('Posted tweet: %s %s %s', topic_choice, note_choice, tweet)

# update count of note that was tweeted, and update history

current.execute("UPDATE NOTES SET count=count+1 WHERE id=?",(note_choice,))
current.execute("INSERT into HISTORY(note_id,topic,timestamp) VALUES(?,?,?)",(note_choice,topic_choice,datetime.now()))
con.commit()

# log number of remaining unposted notes
 
current.execute("SELECT topic from NOTES where count=0")
records = current.fetchall()
logging.info('Note(s) left: %s', len(records))

# close database

current.close()
con.close()
logging.info('Completed')