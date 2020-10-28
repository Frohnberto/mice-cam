from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from picamera import PiCamera
from time import sleep
import os

#def serialUpload():
#    folderName = 'Raspberry Pi'  # Please set the folder name.
#    folders = drive.ListFile(
#    {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
#    for folder in folders:
#        if folder['title'] == folderName:
#            for i in range(2):

#                file_name = 'testfile%i.jpg' %i
#                file1 = drive.CreateFile({'title': file_name , 'parents': [{'id': folder['id']}]})  # Create GoogleDriveFile instance with title 'Hello.txt'.
#                file1.SetContentFile(file_path) # Set content of the file from given string.
#                file1.Upload()
#    print('Upload Successful!')
    
def singleUpload(file_path, file_name):    
    folderName = 'Raspberry Pi'  # Please set the folder name.
    folders = drive.ListFile(
    {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    for folder in folders:
        if folder['title'] == folderName:
            file1 = drive.CreateFile({'title': file_name , 'parents': [{'id': folder['id']}]})  # Create GoogleDriveFile instance with title 'Hello.txt'.
            file1.SetContentFile(file_path) # Set content of the file from given string.
            file1.Upload()
    print('Upload Successful!')

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
drive = GoogleDrive(gauth)
    
newpath = r'/home/pi/Documents/TestPictures'
if not os.path.exists(newpath):
  os.makedirs(newpath)
  print('Ordner erstellt!')
else:
    print('Ordner bereits vorhanden')


camera = PiCamera()
camera.resolution = (2592, 1458)
sleep(10)


camera.awb_mode = 'auto'
sleep(5)
camera.capture('/media/pi/Documents/TestPictures/auto.jpg')
file_path1 = r'/media/pi/Documents/TestPictures/auto.jpg' # Dateipfad für den Upload
file_name1 = 'auto.jpg'

camera.awb_mode = 'shade'
sleep(5)
camera.capture('/media/pi/Documents/TestPictures/shade.jpg')
file_path2 = r'/media/pi/Documents/TestPictures/shade.jpg' # Dateipfad für den Upload
file_name2 = 'shade.jpg'

camera.awb_mode = 'cloudy'
sleep(5)
camera.capture('/media/pi/Documents/TestPictures/cloudy.jpg')
file_path3 = r'/media/pi/Documents/TestPictures/cloudy.jpg' # Dateipfad für den Upload
file_name3 = 'cloudy.jpg'

singleUpload(file_path1, file_name1)
singleUpload(file_path2, file_name2)
singleUpload(file_path3, file_name3)



