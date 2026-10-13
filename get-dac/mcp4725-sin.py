import mcp4725_driver as driver
import signal_generator as sg
import time

amplitude = 3.0
signal_frequency = 10
sampling_frequency = 1000
t = 0

try:
    dac = driver.MCP4725(5.0, 0x61, True)
    while True:
        voltage = amplitude*sg.get_sin_wave_amplitude(signal_frequency, t)
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)
        t+=1/sampling_frequency
finally:
    dac.deinit()