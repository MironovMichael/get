import RPi.GPIO as GPIO
l = [22, 27, 17, 26, 25, 21, 20, 16]
GPIO.setmode(GPIO.BCM)
GPIO.setup(l, GPIO.OUT)
d = 3.18
def voltage_to_number(voltage):
    if not(0.0 <= voltage <= d):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {d:.2f} B")
        print("Устанавливаем 0.00 В")
        return 0
    return int(voltage / d * 255)

def number_to_dac(number):
    k = list(map(int, bin(number)[2::]))
    while len(k)<8:
        k = [0] + k
    GPIO.output(l[::-1], k)

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")
        
finally:
    GPIO.output(l, 0)
    GPIO.cleanup()



