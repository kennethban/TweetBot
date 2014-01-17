## TweetBot - Automated Posting of Notes/Questions
This Python script automates the posting of tweets from a database of notes. It can be used to post notes/questions to aid in the revision of lessons organized by topic.

## Installation
The script requires a [Dropbox](http://www.dropbox.com) account for the files and a [PythonAnywhere](http://www.pythonanywhere.com) account for daily execution of the script

###1.Installation of script and supporting files on Dropbox
- Create a directory in your DropBox account e.g. Dropbox/TweetBot
- Copy all the files into the directory
  
    `tweetbot.py`    
    `tweetbot.db`    
    `tweetbot.cfg`

###2.Setup of PythonAnywere
PythonAnywhere provides many preinstalled Python modules, but does not include the Twitter module `twython` used in this script

- Start bash session
- Install twython module

	`pip install --user twython`

###3.Link Dropbox to PythonAnywhere account
Linking the Dropbox directory that contains the script allows you to edit the `tweetbot.db` database and `tweetbot.cfg` configuration file locally. Changes will be automatically synced to PythonAnywhere which executes the script. For detailed steps, see [instructions](https://www.pythonanywhere.com/wiki/UsingDropbox) provided by PythonAnywhere.

- Share Dropbox account to PythonAnywere
- Go to Dropbox and choose folder to share (e.g. Dropbox/TweetBot)

###4.Set up Twitter authorization
The script requires authorization to access your [Twitter](http://twitter.com) account in order to post tweets.

- Register an [application](https://dev.twitter.com/apps)
- Grant access (read/write) to the application
- Obtain the following 4 tokens

    `Consumer key`    
	`Consumer secret`    
	`Access token`    
	`Access token secret`
   
    
- edit the `tweetbot.cfg` configuration file and fill in the 4 tokens under the `[twitter]` section
```
[twitter]
consumer_token = 
consumer_secret = 
access_token = 
access_secret = 
```

###5. Add notes to database
The `tweetbot.db` SQLite database can be edited using an SQLite editor e.g. [SQLite Database Browser](http://http://sourceforge.net/projects/sqlitebrowser/).

- Open the `NOTES` table in the database
- Add notes/questions (up to 140 characters) in the `note` field
- Add hyperlinks to additional material if needed in the `link` field
- Add a topic name (e.g. diabetes) in the the `topic` field
- Set `count` field to 0

###6. Assign weightage for each topic
Notes are classified by the `topic` field in the `NOTES` table and a weight (1-9) can be assigned to each topic. The distribution of weights will determine the likelihood of a topic being chosen for posting of tweets. 
- Edit the `[topic]` section in the `tweetbot.cfg` configuration file. For example:

```
[topic]
topic1=1    
topic2=9
```

###7. Set up schedule
The days of the week (mon,tue,wed,thu,fri,sat,sun) for posting of tweets can be specified.
- Edit the `[schedule]` section in the `tweetbot.cfg` configuration file. For example:

```
[schedule]   
days=mon,wed,fri,sun
```

###8. Start daily execution of script under PythonAnywhere
    














