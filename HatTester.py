import RPi.GPIO as GPIO
import time
#import os
blueIo = 18
redIo = 10
greenIo = 11
loopBackIo = redIo
buttonIo = 4
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buttonIo, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(redIo,GPIO.OUT)
GPIO.setup(greenIo,GPIO.OUT)
GPIO.setup(blueIo,GPIO.OUT)
GPIO.output(loopBackIo,GPIO.HIGH)
buttonTested = False

def buttonPressed(channel):
    global buttonTested
    GPIO.output(blueIo,GPIO.HIGH)
    GPIO.output(loopBackIo,GPIO.LOW)
    time.sleep(1)
    buttonTested = True
    GPIO.output(blueIo,GPIO.LOW)
    GPIO.output(loopBackIo,GPIO.HIGH)

GPIO.add_event_detect(buttonIo, GPIO.FALLING, callback=buttonPressed)
try:
    while buttonTested == False:
        GPIO.output(loopBackIo,GPIO.HIGH)
        time.sleep(1)
except KeyboardInterrupt:
    print("KeyboardInterrupt")

try:
    #perform loopback test
    while True:
        GPIO.output(loopBackIo,GPIO.HIGH)
        time.sleep(1)
except KeyboardInterrupt:
    print("KeyboardInterrupt")

GPIO.output(redIo,GPIO.LOW)
GPIO.output(greenIo,GPIO.LOW)
GPIO.output(blueIo,GPIO.LOW)
GPIO.cleanup() # clean up GPIO on normal exit

print("Done")
