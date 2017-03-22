import time
import requests
import grovepi
import sys

touch_sensor = 4                           # DHT22 temp & humidity sensor is connected to port D8
url = "http://10.10.98.173:3000/"

grovepi.pinMode(touch_sensor,"INPUT")

while True:
  
  try:
    print(grovepi.digitalRead(touch_sensor))

    sleepval = grovepi.digitalRead(touch_sensor)


    payload = { sleepval }

    requests.post(sleepval, data=payload)    # write data

    time.sleep(2.0)           # 2 second delay

  except KeyboardInterrupt:
    print "Terminating"
    break
  except IOError:
    print "IOError, continuing"
  except:
    print "Unexpected error, continuing"
    print "sys.exc_info()[0]: ", sys.exc_info()[0]

