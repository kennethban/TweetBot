## TweetBot - Automated Posting of Notes for Revision
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

- share Dropbox account to PythonAnywere
- go to Dropbox and choose folder to share (e.g. Dropbox/TweetBot)

###4.Set up Twitter authorization
The script requires authorization to your [Twitter](http://twitter.com) account.

- register an [application](https://dev.twitter.com/apps)
- grant access (read/write) to the application
- obtain the following tokens

	1. `Consumer key`
    2. `Consumer secret`
    3. `Access token`
    4. `Access token secret`
    
- edit the `tweetbot.cfg` configuration file and fill in the 4 tokens
    [twitter]
    consumer_token = 
    consumer_secret = 
    access_token = 
    access_secret = 
    
    
    














