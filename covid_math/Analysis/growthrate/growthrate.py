"""
growthrate.py
Author: Kyle Crandall

Calculate and plot growth rate
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from covid_math.utilities import load_data


if __name__ == '__main__':
    data, locations, dates = load_data()

    data = np.sum(data, axis=0)

    growth_daily = np.stack([data[0, :]] + [data[i+1, :] - data[i, :] for i in range(data.shape[0]-1)], axis=0)
    growth_rate = np.stack([growth_daily[i+1, :]/growth_daily[i, :] for i in range(growth_daily.shape[0]-1)], axis=0)

    plt.figure(1)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=14))

    plt.plot(dates, growth_daily, '.')
    plt.xlabel('date')
    plt.ylabel('daily growth')
    plt.legend(['Confirmed Cases', 'Deaths', 'Recoveries'])

    plt.figure(2)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=14))

    plt.semilogy(dates[1:], growth_rate, '.')
    plt.xlabel('date')
    plt.ylabel('growth rate')
    plt.legend(['Confirmed Cases', 'Deaths', 'Recoveries'])

    plt.show()
