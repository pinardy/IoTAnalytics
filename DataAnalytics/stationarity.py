from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import pandas as pd
import os

'''
http://www.seanabu.com/2016/03/22/time-series-seasonal-ARIMA-model-in-python/

This file is to test if the time-series data is stationary
For stationary data, we can apply regression techniques to the time dependent variable.
'''


# input files
inputFileTemp = "datasets\\mtgrm1_AC\\Temperature (24-28 Apr)- Meeting Room 1 - AC Controller.csv"

# create DataFrame objects
dataTemp = pd.read_csv(inputFileTemp,
                       parse_dates=[0], header=0, usecols=[0, 1])

## Converts date/time data to datetime64 object
dataTemp['Date & Time'] = pd.to_datetime(dataTemp['Date & Time'])
dataTemp = dataTemp.set_index('Date & Time')

## Set time frame from 9am to 6pm
dataTemp = dataTemp.between_time('9:00', '18:00')

## Reset index so that we can plot the graph later
dataTemp.reset_index(inplace = True)


# -=-=-=-=-= Stationarity test -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# -- Function: test_stationarity
# -- Purpose:  Perform stationarity test & Dickey-Fuller test
# -------------------------------------------------------------------

def test_stationarity(timeseries):
    # Determine rolling statistics
    rolmean = pd.rolling_mean(timeseries, window=12)
    rolstd = pd.rolling_std(timeseries, window=12)

    # Plot rolling statistics:
    fig = plt.figure(figsize=(12, 8))
    orig = plt.plot(timeseries, color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label='Rolling Std')

    # Labeling the graphs
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.xlabel('Number of observations')
    plt.ylabel('Temperature ($^\circ$C)')

    # Perform Dickey-Fuller test:
    print '\n---- Results of Dickey-Fuller Test ----'
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical Value (%s)' % key] = value
    print dfoutput

    # Display graph
    print '\nPerforming stationarity test...'
    # plt.show()

    # Save graph to a file called "stationaryTest.png"
    dirPath = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots\\Temperature"
    dirPathFile = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots\\Temperature\\stationaryTest"

    # initialize directory if it doesn't exist
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)

    plt.savefig(dirPathFile + ".png")

test_stationarity(dataTemp['Value'])