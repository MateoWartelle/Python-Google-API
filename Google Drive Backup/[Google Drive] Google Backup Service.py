from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from os import listdir
from os.path import isfile, join
import os

""" Lists all files in your google drive's root directory by title, id """
def listing_google_drive_files():
    settings_path = 'settings.yaml'
    gauth = GoogleAuth(settings_file=settings_path)
    drive = GoogleDrive(gauth)
    file_list = drive.ListFile({'q': "'root' in parents"}).GetList()
    for file1 in file_list:
        print(file1['title'], file1['id'])

""" Attempts to upload a file if name exists then it deletes the existing file
    and processes the upload """
def upload_to_google_drive(file):
    settings_path = 'settings.yaml'
    gauth = GoogleAuth(settings_file=settings_path)
    drive = GoogleDrive(gauth)
    file_list = listing_google_drive_files()
    try:
        for file1 in file_list:
            if file1['title'] == file:
                file1.Delete()
        f = drive.CreateFile()
        f.SetContentFile(file)
        f.Upload()
        print (file, "uploaded")
    except:
        pass
""" Pushes all files in current working directory to be uploaded to google drive """
def backup_to_google_drive():
    ListofFiles = os.listdir('.')
    for i in ListofFiles:
        upload_to_google_drive(i)
