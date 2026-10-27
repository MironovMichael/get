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
    
    def succesive_approximation_adc(self):
        left, right = 0, 255
        while left < right:
            mid = (left + right) // 2
            
            self.number_to_dac(mid)
            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio) == 1:
                right = mid
            else:
                left = mid+1
        return left

    def get_sc_voltage(self):
        number = self.sequential_counting_adc()
        voltage = number / 255 * self.dynamic_range
        return voltage

    def get_sar_voltage(self):
        return self.succesive_approximation_adc() * self.dynamic_range / 255

if __name__ == "__main__":
    dac = None
    try:
        dac = R2R_ADC(3.290)
        while True:
            voltage = dac.get_sar_voltage()
            print(f"Напряжение: {voltage:.3f} B")
    finally:
        if dac is not None:
            dac.deinit()


