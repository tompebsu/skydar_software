#!/usr/bin/env python 

import csv
import serial
from datetime import datetime
from time import sleep
from mpu6050 import mpu6050
mpu = mpu6050(0x68)

#Garmin lidar-lite
ser_lidar = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
#GPS-serial 
ser_gps = serial.Serial(
port = '/dev/ttyACM1',
baudrate = 115200,
parity=serial.PARITY_NONE,
stopbits = serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)

header = ['date','month','year','hour','minute','second','temperature','ax','ay','az','gx','gy','gz','GPGGA','time','latitude','N_S','longitude',
          'E_W','fix_quality','NumberOfSatellites','HorizaontalDilution','altitude','Meter','HeightofGeoidAboveWGS84','M','Blank','checksum','GarminLidar']
with open('skydar_12_09_2022.csv','a') as f:
    writer = csv.writer(f)
    writer.writerow(header)

while True:
    
    f = open('skydar_12_09_2022.csv','a')    
    writer = csv.writer(f)
    
    
    now = datetime.now()
    #mpu6050
    accel_data = mpu.get_accel_data()
    a_x = str(accel_data['x'])
    a_y = str(accel_data['y'])
    a_z = str(accel_data['z'])
    
    gyro_data = mpu.get_gyro_data()
    g_x = str(gyro_data['x'])
    g_y = str(gyro_data['y'])
    g_z = str(gyro_data['z'])
    
    
    temperature = str(mpu.get_temp())
    #raspberri time
                    
    date = now.strftime("%d")
    month = now.strftime("%m")
    year = now.strftime("%y")
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    second = now.strftime("%S")
    
    print(date,month,year,hour,minute,second,temperature,a_x,a_y,a_z,g_x,g_y,g_z)
    GPS=str(ser_gps.readline().decode('utf-8').rstrip())
    print (GPS)
    line = ser_lidar.readline().decode('utf-8').rstrip()
    print(line)
    

    f.write(date+",")
    f.write(month+",")
    f.write(year+",")
    f.write(hour+",")
    f.write(minute+",")
    f.write(second+",")
    f.write(temperature+",")
    f.write(a_x+","+a_y+","+a_z+","+g_x+","+g_y+","+g_z+",")
    f.write(GPS+",")
    f.write(line+",")
    sleep(1) 
            
    f.write('\n')




