import time
import requests
import grovepi
import sys

touch_sensor = 4
green_led = 5
red_led = 3
url = "http://10.10.89.3:3000/echo"

grovepi.pinMode(touch_sensor,"INPUT")
grovepi.pinMode(green_led, "OUTPUT")
grovepi.pinMode(red_led, "OUTPUT")

while True:
    
    
    sleep_val = grovepi.digitalRead(touch_sensor)

    if sleep_val == 1:
        try:
            print "On"
            grovepi.digitalWrite(green_led, 1)
            grovepi.digitalWrite(red_led, 0)
            



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
        print "Off"
        grovepi.digitalWrite(green_led, 0)
        grovepi.digitalWrite(red_led, 1)
        


        
    
    

    
    
