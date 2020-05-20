"""
covid_plot.py
Author: Kyle Crandall

Plot US Covid Data.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from covid_math.utilities import load_data

if __name__ == '__main__':
    data, locations, dates = load_data()

    us_data = np.zeros((data.shape[1], 3))

    for i, loc in enumerate(locations):
        if loc[1] == 'US':
            us_data += data[i, :, :]

    growth_daily = np.stack([us_data[0, :]] + [us_data[i + 1, :] - us_data[i, :] for i in range(us_data.shape[0] - 1)],
                            axis=0)
    active_cases = us_data[:, 0] - us_data[:, 1] - us_data[:, 2]

    plt.figure(1)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=28))

    plt.plot(dates, us_data, '.')
    plt.xlabel('date')
    plt.legend(['Confirmed Cases', 'Deaths', 'Recoveries'])

    plt.figure(2)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=28))

    plt.semilogy(dates, us_data, '.')
    plt.xlabel('date')
    plt.legend(['Confirmed Cases', 'Deaths', 'Recoveries'])

    plt.figure(3)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=28))

    ax.fill_between(dates, 0, us_data[:, 0])
    ax.fill_between(dates, 0, us_data[:, 1] + us_data[:, 2])
    ax.fill_between(dates, 0, us_data[:, 2])
    plt.xlabel('date')
    plt.legend(['active cases', 'dead', 'recoveries'], loc='upper left')

    plt.figure(4)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=28))

    plt.semilogy(dates, growth_daily, '.')
    # plt.plot(dates, growth_daily, '.')
    plt.xlabel('date')
    plt.ylabel('daily growth')
    plt.legend(['Confirmed Cases', 'Deaths', 'Recoveries'])

    plt.figure(5)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=28))

    plt.plot(dates, active_cases, '.')
    # plt.semilogy(dates, active_cases, '.')
    plt.xlabel('date')
    plt.ylabel('active cases')

    plt.show()
