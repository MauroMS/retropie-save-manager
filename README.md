# retropie-save-manager
I'm trying to create a couple of Python scripts to Upload/Download my saves from/to my dropbox account, so I can play in different devices with the most updated game save :)

PS: I haven't tested on my pi yet. I'll test it asap.

Hot to use it:
First, Create a new app on Dropbox:
Navigate to https://www.dropbox.com/developers/apps
Login to your account
Click on "Create App" button
Select Permission type - I used app folder, as I don't need access to all folders.
Name your app

Second, Go to your app settings and generate a Token under OAuth 2 section.
ps: I don;t know how long they last for, but as I know almos nothing about Python, I'm not going to implement OAuth2 properly at the moment.

Once you generated the Token, just replace it on the script.

References I used to create my scripts:
https://www.dropbox.com/developers/apps
https://github.com/dropbox/dropbox-sdk-python/blob/master/example/back-up-and-restore/backup-and-restore-example.py
https://github.com/FreakyBigFoot/PiSave/blob/master/Backup.py
