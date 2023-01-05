from bluedot import BlueDot
from time import sleep
import RPi.GPIO as GPIO
from signal import pause
import csv
from datetime import datetime
import serial


#Stepper motor set up 
DIR = 20 # Direction GPIO Pin
STEP = 21 #Step GPIO Pin
CW = 1 #Clockwise Rotation
CCW = 0 #Counterclockwise Roation
SPR =200 #Steps per Revolution (360/1.8)


GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

MODE = (14,15,16)
GPIO.setup(MODE,GPIO.OUT)
RESOLUTION = {'Full':(0,0,0),'Half':(1,0,0),'1/4':(0,1,0),'1/8':(1,1,0),'1/32':(1,0,1)}

GPIO.output(MODE, RESOLUTION['1/32'])
#GPIO.output(MODE, RESOLUTION['Full'])

step_count = SPR*150 #how many step (distance)-rotation?
#step_count = SPR*125 #how many step (distance)-rotation? 

delay = (1/SPR)*(90/100) #delay speed
#delay = (1/SPR)*(1/25)
#########

ser = serial.Serial(
port = '/dev/ttyACM0',
#port = '/dev/ttyAMA0',
#port = '/dev/ttyS0',

baudrate = 115200,
parity=serial.PARITY_NONE,
stopbits = serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)
conter = 0   
#########
header = ['date','month','year','hour','minute','second','GPGGA','time','latitude','N_S','longitude',
          'E_W','fix_quality','NumberOfSatellites','HorizaontalDilution','altitude','Meter','HeightofGeoidAboveWGS84','M','Blank','checksum']
with open('rt_12_09_2022_T1.csv','a') as f:
    writer = csv.writer(f)
    writer.writerow(header)


    now = datetime.now()
    date = now.strftime("%d")
    month = now.strftime("%m")
    year = now.strftime("%y")
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    second = now.strftime("%S")
    GPS=str(ser.readline())

    f.write(date+",")
    f.write(month+",")
    f.write(year+",")
    f.write(hour+",")
    f.write(minute+",")
    f.write(second+",")
    f.write(GPS+",")
    f.write('\n')
#######  
GPIO.output(DIR, CCW)
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

sleep(5)
GPIO.output(DIR, CW)
for x in range(step_count):
         GPIO.output(STEP, GPIO.HIGH)
         sleep(delay)
         GPIO.output(STEP, GPIO.LOW)
         sleep(delay)


with open('rt_12_09_2022_T1.csv','a') as f:
    writer = csv.writer(f)

    now = datetime.now()
    date = now.strftime("%d")
    month = now.strftime("%m")
    year = now.strftime("%y")
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    second = now.strftime("%S")
    GPS=str(ser.readline())
    
    f.write(date+",")
    f.write(month+",")
    f.write(year+",")
    f.write(hour+",")
    f.write(minute+",")
    f.write(second+",")
    f.write(GPS+",")
    f.write('\n')
