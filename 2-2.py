import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
number = [1,0,0,0,0,0,0,0]
if len(dac) == len(number):
    GPIO.setup(dac, GPIO.OUT)
    for i in range(0,8,1):
        GPIO.output(dac[i], number[i])
    time.sleep(15)

GPIO.output(dac, 0)
GPIO.cleanup()
