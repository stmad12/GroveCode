import time
import requests
import grovepi
import sys

touch_sensor = 4
led = 5
url = "http://10.10.89.3:3000/echo"

grovepi.pinMode(touch_sensor,"INPUT")
grovepi.pinMode(led, "OUTPUT")

while True:
    
    print(grovepi.digitalRead(touch_sensor))
    
    sleep_val = grovepi.digitalRead(touch_sensor)

    if sleep_val == 1:
        try:
            print "led on"
            grovepi.digitalWrite(led, 1)



            payload = { 'LED On' : sleep_val }

            requests.post(url, data=payload)
    
            time.sleep(.1)

        except KeyboardInterrupt:
            print "Terminating"
            break
        except IOError:
            print "Push/Pull Error, continuing"
        except:
            print "Unexpected error, continuing"
            print "sys.exc_info()[0]: ", sys.exc_info()[0]
        
    else:
        print "led off"
        grovepi.digitalWrite(led, 0)


        
    
    

    
    
