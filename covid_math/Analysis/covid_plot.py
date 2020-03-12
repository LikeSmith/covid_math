"""
covid_plot.py
Author: Kyle Crandall

Plot Raw Covid Data.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from covid_math.utilities import load_data


if __name__ == '__main__':
    data, locations, dates = load_data()

    data = np.sum(data, axis=0)

    plt.figure(1)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=14))

    plt.plot(dates, data, '.')
    plt.xlabel('date')
    plt.legend(['Confirmed Cases', 'Deaths', 'Recoveries'])

    plt.figure(2)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=14))

    plt.semilogy(dates, data, '.')
    plt.xlabel('date')
    plt.legend(['Confirmed Cases', 'Deaths', 'Recoveries'])

    plt.show()
