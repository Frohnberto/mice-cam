import dropbox
from picamera import PiCamera
from time import sleep
import os



dbx = dropbox.Dropbox('RJhMcFceZ30AAAAAAAAAAZCVRK0mdF-0g1CNt9y3gwqhk8wP95-rowt9GcjPgWNo')
#dbx.users_get_current_account()
#file_path = 
#dbx.files_upload("testfile2", '\test2.odt')

#for entry in dbx.files_list_folder('').entries:
#    print(entry.name)





    



    
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

camera.awb_mode = 'shade'
sleep(5)
camera.capture('/media/pi/Documents/TestPictures/shade.jpg')

camera.awb_mode = 'cloudy'
sleep(5)
camera.capture('/media/pi/Documents/TestPictures/cloudy.jpg')

with open('/media/pi/Documents/TestPictures/cloudy.jpg' , "rb") as f:
    dbx.files_upload(f.read(), '/cloudy.jpg')
with open('/media/pi/Documents/TestPictures/shade.jpg' , "rb") as f:
    dbx.files_upload(f.read(), '/shade.jpg')
with open('/media/pi/Documents/TestPictures/auto.jpg' , "rb") as f:
    dbx.files_upload(f.read(), '/auto.jpg')