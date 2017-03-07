import time
import requests
import grovepi
import sys

dht11_port = 8
url = "http://10.10.90.6:3000/dht?key=HFJLASKH"

while True:

    try:

        [temp, humi] = grovepi.dht(dht11_port, 0)

        print(temp, "c")
        print(humi, "%")

        payload = { 'h' : humi, 't' : temp }

        requests.post(url, data=payload)

        time.sleep(2.0)
    except KeyboardInterrupt:
        print "Terminating"
        break
    except IOError:
        print "IOError, continuing"
    except:
        print "Unexpected error, continuing"
        print "sys.exc_info()[0]: ", sys.exc_info()[0]
