import RPi.GPIO as GPIO
class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)

        

    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()
    def set_number(self, number):
        k = list(map(int, bin(number)[2::]))
        while len(k)<8:
            k = [0] + k
        GPIO.output(self.gpio_pin, k)
        print(k)
    def set_voltage(self, voltage):
        if not(0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {d:.2f} B")
            print("Устанавливаем 0.00 В")
            self.set_number(0)
        z = int(voltage / self.dynamic_range * 255)
        self.set_number(z)