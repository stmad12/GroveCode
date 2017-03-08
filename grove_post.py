import time
import requests
import grovepi
import sys

potentiometer = 2
url = "http://10.10.900.72:3000/"

while True:

    try:

        value = grovepi.analogRead(potentiometer)

        print(value)

        payload = { value }
        
        requests.post(url, data=payload)  

        time.sleep(2.0)

    except IOError:
        print "IOError, continuing"
    except:
        print "Unexpected error, continuing"
        print "sys.exc_info()[0]: ", sys.exc_info()[0]
    
