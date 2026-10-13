import pwm_dac
import signal_generator as sg
import time

amplitude = 3.298
signal_frequency = 10
sampling_frequency = 1000
t = 0

try:
    dac = pwm_dac.PWM_DAC(12, 500, 3.298, True)

    while True:
        voltage = amplitude*sg.get_triangle_wave_amplitude(signal_frequency, t)
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)
        t+=1/sampling_frequency
finally:
    dac.deinit()
