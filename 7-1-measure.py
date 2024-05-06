import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time
#Настройка GPIO, GPIO пинов
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

bits= len(dac)

levels = 2**bits

maxVoltage = 3.3

troykamodule = 13

comp =14

GPIO.setup(comp,GPIO.IN)
GPIO.setup(troykamodule, GPIO.OUT, initial = GPIO.HIGH)

#Функция вывода двоичного числа и функция вывода сигнала
def decimal2binary(chislo):
    return [int(element) for element in bin(chislo)[2:].zfill(8)]
def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac,signal)
    return signal

#Создаем пустой массив для заполнения значениями
measured_data=[]
vremya=0.01

#Исполняемая часть
try:
    value=0
    start_time = time.time()
    while value<200:
        value =0
        #Цикл пробегающий все значения на DAC
        for i in range(8):
            value+=int( 2**(7-i))
            signal = num2dac(value)
            
            time.sleep(vremya)
            comparatorValue = GPIO.input(comp)
            value-=comparatorValue*int( 2**(7-i))
        #Перевод значения в вольты
        voltage = value/levels*maxVoltage
        if (value>0) and  (value < 210):
            measured_data.append(value)
        print("ADC value = {:^3} -> {}, input voltage = {: .2f}".format(value,signal,voltage))
    end_time = time.time()
    #Вычисление продолжительности, периода измерения и частоты
    duration = end_time - start_time
    frequency = len(measured_data) / duration
    period = 1/frequency
except KeyboardInterrupt:
    print('Программа была остановлена с клавиатуры')

#Завершающая часть скрипта
finally:
    #Делаем вывод в файл построчно
    measured_datastr=[str(item) for item in measured_data]
    with open("data.txt","w") as outfile:
        outfile.write("\n".join(measured_datastr))
    #Строим график на основе полученного массива
    plt.plot(measured_data)
    #Отчистка
    GPIO.output(dac, 0)                                                                                                                                                                                                                                                               
    GPIO.cleanup(dac)
    #Вывод в терминал и файл settings.txt
    print(duration,'секунд измерений')
    print(period,' секунд на одно измерение')
    print('Частота дискретизации' ,frequency, 'измерений в секунду')
    print('Шаг квантования' , round(maxVoltage/256,4))
    with open("settings.txt","w") as outfile:
        outfile.write(str(maxVoltage/256)+'\n'+str(frequency))
    #Вывод изображения 
    plt.show()
