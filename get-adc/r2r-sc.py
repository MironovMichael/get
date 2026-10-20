import time
from r2r_adc import R2R_ADC
import adc_plot

dr = 3.3
du = 3.0

def main():
    adc = None
    voltage_values = []
    time_values = []
    try:
        adc = R2R_ADC(dr, compare_time=0.0001)
        start = time.time()
        while time.time()-start < du:
            voltage_values.append(adc.get_sc_voltage())
            time_values.append(time.time() - start)
    finally:
        if adc is not None:
            adc.deinit()

    if time_values:
        adc_plot.plot_voltage_vs_time(time_values, voltage_values, dr)
        adc_plot.plot_sampling_period_hist(time_values)

if __name__ == '__main__':
    main()