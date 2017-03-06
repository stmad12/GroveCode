

import time
import grovepi

led = 7

grovepi.pinMode(led, "OUTPUT")
time.sleep(1)
i = 0

while True:
    try:
        
