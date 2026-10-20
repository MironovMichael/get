import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.title("Зависимость напряжения от времени")
    plt.xlim(left=0)
    plt.ylim(0, max_voltage)
    plt.grid(True)
    plt.show()

def plot_sampling_period_hist(time):
    sampling_periods = [time[i] - time[i-1] for i in range(1, len(time))]
    plt.figure(figsize=(10,6))
    plt.hist(sampling_periods)
    plt.xlabel("Промежуток между измерениями, с")
    plt.ylabel("Количество измерений")
    plt.title("Гистограмма периодов измерений")
    plt.xlim(0, 0.06)
    plt.grid(True)
    plt.show()