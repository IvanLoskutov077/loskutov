import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

def dec2bin(dec_number):
    return [int(bit) for bit in bin(dec_number)[2:].zfill(8)]

try:
    T = float(input("Введите период треугольного сигнала (в секундах): "))
    
    while True:
        for value in range(0, 256):
            GPIO.output(dac, dec2bin(value))
            time.sleep(T / 256)
        for value in range(255, -1, -1):
            GPIO.output(dac, dec2bin(value))
            time.sleep(T / 256)
            
except KeyboardInterrupt:
    print("Программа завершена.")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()