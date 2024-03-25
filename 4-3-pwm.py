import RPi.GPIO as GPIO
pwm_pin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, 100) 

try:
    pwm.start(0)

    while True:
        duty_cycle = float(input("Введите коэффициент заполнения (от 0 до 100): "))
        duty_cycle = max(0, min(100, duty_cycle))
        pwm.ChangeDutyCycle(duty_cycle)
        voltage = duty_cycle / 100 * 3.3
        print(f"Предполагаемое напряжение на выходе RC-цепи: {voltage:.2f} Вольт")

except KeyboardInterrupt:
    print("\nПрограмма завершена.")
finally:
    pwm.stop()
    GPIO.cleanup()