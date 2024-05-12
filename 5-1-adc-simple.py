import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
def decimal2binary(chislo):
    return [int(el) for el in bin(chislo)[2:].zfill(8)]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
bits = len(dac)
levels = 2**(bits)
maxVoltage = 3.3
troykamodule = 13
comp =14
GPIO.setup(comp,GPIO.IN)
GPIO.setup(troykamodule, GPIO.OUT, initial = GPIO.HIGH)

def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac,signal)
    return signal

try:
    while True:
        for value in range(256):
            signal = num2dac(value)
            time.sleep(0.0001)
            voltage = (value/levels)*maxVoltage
            comparatorValue = GPIO.input(comp)
            if comparatorValue == 1:
                print(f"Значение на АЦП = {value}, напряжение ={voltage: .2f}В")
                break
except KeyboardInterrupt:
    print('\nStopped')

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()