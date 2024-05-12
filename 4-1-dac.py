import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

def dec2bin_list(dec_number):
    return [int(bit) for bit in bin(dec_number)[2:].zfill(8)]

try:
    while True:
        user_input = input("Введите число от 0 до 255 или 'q' для выхода: ")
        
        if user_input.lower() == 'q':
            break
        
        try:
            dec_number = int(user_input)
            
            if dec_number < 0:
                print("Введите неотрицательное число.")
                continue
            elif dec_number > 255:
                print("Число превышает 255.")
                continue
            bin_list = dec2bin_list(dec_number)
            GPIO.output(dac, bin_list)
            voltage = dec_number / 255 * (3.3)
            print(f"Предполагаемое напряжение: {voltage:.2f} Вольт")  
        except ValueError:
            print("Ошибка: Введите целое число.")
        
        except KeyboardInterrupt:
            print("Программа завершена.")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
