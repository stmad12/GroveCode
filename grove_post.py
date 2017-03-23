import time
import requests
import grovepi
import sys

touch_sensor = 4                           # DHT22 temp & humidity sensor is connected to port D8
url = "http://10.10.89.3:3000/echo"

grovepi.pinMode(touch_sensor,"INPUT")

while True:
  
  try:
    print(grovepi.digitalRead(touch_sensor))

    sleep_val = grovepi.digitalRead(touch_sensor)


    payload = { 'sleep' : sleep_val }

    requests.post(url, data=payload)    # write data

    time.sleep(.25)           # 2 second delay

  except KeyboardInterrupt:
    print "Terminating"
    break
  except IOError:
    print "Push/Pull Error, continuing"
  except:
    print "Unexpected error, continuing"
    print "sys.exc_info()[0]: ", sys.exc_info()[0]
