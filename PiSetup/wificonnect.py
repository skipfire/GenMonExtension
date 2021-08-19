import RPi.GPIO as GPIO
import time
import os
import urllib.request
blueIo = 18
redIo = 10
greenIo = 11
buttonIo = 4
ledIo = blueIo
wifiConnectOn = False
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buttonIo, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(redIo,GPIO.OUT)
GPIO.setup(ledIo,GPIO.OUT)
def testConnected():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False
def buttonPressed(channel):
    global wifiConnectOn
    if wifiConnectOn :
        return
    GPIO.output(ledIo,GPIO.HIGH)
    time.sleep(1)
    wifiConnectOn = True
    os.system('wifi-connect -a 300 -s PiGen')
    wifiConnectOn = False
    GPIO.output(ledIo,GPIO.LOW)
GPIO.add_event_detect(buttonIo, GPIO.FALLING, callback=buttonPressed)
try:
    while True:
        if testConnected() == False and wifiConnectOn == False :
            GPIO.output(redIo,GPIO.HIGH)
        else :
            GPIO.output(redIo,GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    print("KeyboardInterrupt")
GPIO.cleanup() # clean up GPIO on normal exit
print("Done")
