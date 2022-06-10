import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

try:
    while True:
        if document.getElementById('buffer-box-').innerText == "55 BD" :            
            GPIO.output(40,True)
            time.sleep(5)			
            GPIO.output(40,False)   
        elif buffer == "BD BD" :
            GPIO.output(38,True)
            time.sleep(5)
            GPIO.output(38,False)
        elif buffer == "BD E9" :
            GPIO.output(37,True)
            time.sleep(5)
            GPIO.output(37,False)
        else:
            GPIO.output(40,True)
            GPIO.output(38,True)
            GPIO.output(37,True)

finally:
# cleanup the GPIO before finishing :)
    GPIO.cleanup()