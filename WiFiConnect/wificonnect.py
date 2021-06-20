import RPi.GPIO as GPIO
import time
import os
blueIo = 17
redIo = 27
greenIo = 22
buttonIo = 5
ledIo = blueIo
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buttonIo, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def buttonPressed(channel):
    GPIO.setup(ledIo,GPIO.OUT)
    GPIO.output(ledIo,GPIO.HIGH)
    time.sleep(1)
    os.system('wifi-connect -a 300 -s PiGen')
    GPIO.output(ledIo,GPIO.LOW)
GPIO.add_event_detect(buttonIo, GPIO.FALLING, callback=buttonPressed)
try:
    while True:
        time.sleep(1)
    # raw_input("Waiting for button...\n>")
except KeyboardInterrupt:
    print "KeyboardInterrupt"
GPIO.cleanup()           # clean up GPIO on normal exit
print "Done"
