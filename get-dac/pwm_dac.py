import RPi.GPIO as GPIO
class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(gpio_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(gpio_pin, pwm_frequency)
        self.pwm.start(0)

        

    def deinit(self):
        GPIO.cleanup()
        
    def set_voltage(self, voltage):
        if not(0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} B")
            print("Устанавливаем 0.00 В")
            self.pwm.ChangeDutyCycle(0)
        else:
            duty_cycle = voltage / self.dynamic_range * 100
            self.pwm.ChangeDutyCycle(duty_cycle)

if __name__ == "__main__":

    dac = PWM_DAC(12, 500, 3.298, True)
    try:

        while True:
            try:
                voltage = float(input("Введите напряжение: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число, попробуйте ещё раз\n")
    finally:
        dac.deinit()
