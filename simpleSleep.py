'this will be a proof-of-concept script for using the touch sensor to shut down all other sensors'


import time
import grovepi

# Connect the Grove Touch Sensor to digital port D4
# SIG,NC,VCC,GND
touch_sensor = 4

grovepi.pinMode(touch_sensor,"INPUT")

while True:
    try:
        print(grovepi.digitalRead(touch_sensor))
        

    except IOError:
        print ("Error")

while touch_sensor == 1:
    'Execute the rest of the code while the sensor has operator presence'
