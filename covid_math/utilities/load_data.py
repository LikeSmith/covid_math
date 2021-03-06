"""
load_data.py
Author: Kyle Crandall

Load covid data from https://github.com/CSSEGISandData/COVID-19.
"""

import os
import csv
import datetime
import numpy as np

PATH_TO_DATA_REPO = r"D:\Users\Kyle\Documents\COVID-19\\"
PATH_TO_DATA_DIR = r"csse_covid_19_data\csse_covid_19_daily_reports\\"


def load_data(path=PATH_TO_DATA_REPO+PATH_TO_DATA_DIR):
    data = []
    dates = []
    locations = []

    # Load data from files
    for filename in os.listdir(path):
        if filename.find('.') != -1 and filename.split('.')[-1] == 'csv':
            dates.append(datetime.datetime.strptime(filename.split('.')[0], '%m-%d-%Y').date())
            with open(path+filename, 'r') as f:
                csv_reader = csv.reader(f)
                data.append(np.zeros((len(locations), 3)))
                skip_first_row = True
                conf_i = 3
                dead_i = 4
                reco_i = 5
                data_fmt = 1

                for row in csv_reader:
                    if skip_first_row:
                        skip_first_row = False

                        for i, item in enumerate(row):
                            if item == 'Confirmed':
                                conf_i = i
                            elif item == 'Deaths':
                                dead_i = i
                            elif item == 'Recovered':
                                reco_i = i

                        if 'Admin2' in row:
                            data_fmt = 2
                        else:
                            data_fmt = 1
                        continue

                    if row[conf_i] == '':
                        row[conf_i] = '0'
                    if row[dead_i] == '':
                        row[dead_i] = '0'
                    if row[reco_i] == '':
                        row[reco_i] = '0'

                    if data_fmt == 1:
                        loc = row[0:2]
                    else:
                        loc = row[2:4]
                    if loc in locations != -1:
                        i = locations.index(loc)
                        data[-1][i, 0] += float(row[conf_i])
                        data[-1][i, 1] += float(row[dead_i])
                        data[-1][i, 2] += float(row[reco_i])
                    else:
                        data[-1] = np.concatenate([data[-1], np.zeros((1, 3))], axis=0)
                        locations.append(loc)
                        data[-1][-1, 0] += float(row[conf_i])
                        data[-1][-1, 1] += float(row[dead_i])
                        data[-1][-1, 2] += float(row[reco_i])

    # Pad data frames with zeros and stack into single array
    n_locations = len(locations)
    data = [d if d.shape[0] == n_locations else np.concatenate([d, np.zeros((n_locations-d.shape[0], 3))]) for d in data]
    data = np.stack(data, axis=1)

    # Sort Data based on date
    sort_ind = np.argsort(dates)
    dates = [dates[i] for i in sort_ind]
    data = data[:, sort_ind, :]

    return data, locations, dates


if __name__ == '__main__':
    print('Testing Loader....')

    data, locations, dates = load_data()

    print(data.shape)
    print(len(locations))
    print(len(dates))
