#Using Dropbox API V2

import os, re
import sys
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

#Variables
#File types to backup
filetypes = ('\.state$|\.state\d|\.srm$|\.dat$|\.nv$|\.hi$|\.hs$|\.cfg$|\.fs$|\.eep$')
#Path on Dropbox - In this case, a save folder will be created inside your "App folder" on Dropbox
backup_location = '/Saves'
#Windows - just for development purpose -You can ignore it
#rootdir = '<SAVES-LOCATION>' #r'C:\Users\mschapa\Desktop\Pi'
#Mac
rootdir = '<SAVES-LOCATION>' #'/Users/MauroMS/Desktop/pi/saves'
#Dropbox Token
TOKEN = '<YOUR-TOKEN>';

#Variables to check upload progress
files_to_upload = 0
uploaded_files = 0

# Check for an access token
if (len(TOKEN) == 0):
    sys.exit("ERROR: Looks like you didn't add your access token. "
        "Open up backup-and-restore-example.py in a text editor and "
        "paste in your token in line 14.")

print("Creating a Dropbox object...")
dbx = dropbox.Dropbox(TOKEN)

# Check that the access token is valid
try:     
    dbx.users_get_current_account()
except AuthError as err:
    sys.exit("ERROR: Invalid access token; try re-generating an "
        "access token from the app console on the web.")

for root, dirs, files in os.walk(rootdir):
    for saves in files:
        if re.search(filetypes, saves):
            files_to_upload += 1
print(str(files_to_upload) + ' Files Found')

# Create a backup of the current save files
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        #Get Directory Name
        currentemulatorfolder = os.path.basename(subdir)
        backup_path = backup_location + os.sep + currentemulatorfolder + os.sep + file
        #print(backup_path)
        if re.search(filetypes,file):
            #print(filepath)
            with open(filepath, 'rb') as f:
                try:
                    dbx.files_upload(f.read(), backup_path, mode=WriteMode('overwrite'))
                    uploaded_files += 1
                    print(str(uploaded_files) + '/' + str(files_to_upload) + ' files uploaded')
                except ApiError as err:
                    # This checks for the specific error where a user doesn't have
                    # enough Dropbox space quota to upload this file
                    if (err.error.is_path() and err.error.get_path().error.is_insufficient_space()):
                        sys.exit("ERROR: Cannot back up; insufficient space.")
                    elif err.user_message_text:
                        print(err.user_message_text)
                        sys.exit()
                    else:
                        print(err)
                        sys.exit()
                    print(filepath)

