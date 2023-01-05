#cameratest + motor

import gphoto2 as gp
from time import sleep
from datetime import datetime

camera = gp.Camera()

i = 0
while(1):
    camera.init()
    now = datetime.now()

    date = now.strftime("%d")
    month = now.strftime("%m")
    year = now.strftime("%y")
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    second = now.strftime("%S")

    file_path = camera.capture(gp.GP_CAPTURE_IMAGE)
    target = '/home/pi/camera_pics/capt'+ hour + minute +second + '_'+str(i) + '.jpg' 
    camera_file = camera.file_get(file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
    camera_file.save(target)
    camera.exit()
    sleep(1)
    i = i + 1

