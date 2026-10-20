import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
       GPIO.output(self.bits_gpio, [0]*8)
       GPIO.cleanup()

    def number_to_dac(self, number):
        bits = [(number >> (7-i)) & 1 for i in range(8)]
        GPIO.output(self.bits_gpio, bits)

    def sequential_counting_adc(self):
        for number in range(256):
            self.number_to_dac(number)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == 1:
                return number
        return 255

    def get_sc_voltage(self):
        number = self.sequential_counting_adc()
        voltage = number / 255 * self.dynamic_range
        return voltage

if __name__ == "__main__":
    try:
        dac = R2R_ADC(3.3)
        while True:
            voltage = dac.get_sc_voltage()
            print(f"Напряжение: {voltage:.3f} B")
    finally:
        dac.deinit()


