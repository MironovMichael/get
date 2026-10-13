import math
import time

def get_sin_wave_amplitude(freq, t):
    return (math.sin(2*math.pi*freq*t)+1)/2

def get_triangle_wave_amplitude(freq, t):
    period = 1/freq
    phase = (t%period)/period

    if phase < 0.5:
        return phase*2
    else:
        return (1-phase)*2

def wait_for_sampling_period(sampling_frequency):
    time.sleep(1/sampling_frequency)
    