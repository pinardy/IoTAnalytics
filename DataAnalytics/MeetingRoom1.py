import matplotlib.pyplot as plt
import pandas as pd
import os

# -=-=-= Meeting room 1, sensor 1 -=-=-=

'''
----- DataFrame objects -----
"header = 0" means '0' index is the header
"parse_dates=[0]" converts the Strings under the first column into datetime64 objects
'''

dataTemp = pd.read_csv("datasets\\Temperature (15-31 Mar)- Meeting Room 1 - Sensor 1.csv",
                       parse_dates=[0], header=0, usecols=[0, 1])
dataHumidity = pd.read_csv("datasets\\Humidity (15-31 Mar)- Meeting Room 1 - Sensor 1.csv",
                           parse_dates=[0], header=0, usecols=[0, 1])


# -=-=-=-=-= PRINTING OF DATA -=-=-=-=-=
# print data
# print data['Date & Time']
# print data['Value']
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


# -=-=-=-=-= TEMPERATURE -=-=-=-=-=

def lineGraphTemp():
    plt.plot(dataTemp['Date & Time'], dataTemp['Value'], linestyle='-', color='b')
    plt.xticks(rotation='vertical')

    # Labeling the graphs
    title = "Temperature against Date"
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Temperature')

    # Save graph to a file called "graph.png"
    dirPath = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots\\Temperature"
    dirPathFile = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots\\Temperature\\linegraph"

    # initialize directory if it doesn't exist
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)

    plt.savefig(dirPathFile + ".png")


def boxPlotTemp():
    dataTemp.plot.box()
    color = dict(boxes='DarkGreen', whiskers='DarkOrange',
                 medians='DarkBlue', caps='Gray')
    dataTemp.plot.box(color=color, sym='r+')

    # Labeling the graphs
    title = "Boxplot of temperature in a week"
    plt.title(title)
    plt.xlabel('')
    plt.ylabel('Temperature')

    # Save graph to a file called "boxplot.png"
    dirPath = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots\\Temperature"
    dirPathFile = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots\\Temperature\\boxplot"

    # initialize directory if it doesn't exist
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)

    plt.savefig(dirPathFile + ".png")


# -=-=-=-=-= HUMIDITY -=-=-=-=-=

def lineGraphHumidity():
    plt.plot(dataHumidity['Date & Time'], dataHumidity['Value'], linestyle='-', color='b')
    plt.xticks(rotation='vertical')

    # Labeling the graphs
    title = "Humidity against Date"
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Humidity')

    # Save graph to a file called "graph.png"
    dirPath = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots\\Humidity"
    dirPathFile = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots\\Humidity\\linegraph"

    # initialize directory if it doesn't exist
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)

    plt.savefig(dirPathFile + ".png")


def boxPlotHumidity():
    dataHumidity.plot.box()
    color = dict(boxes='DarkGreen', whiskers='DarkOrange',
                 medians='DarkBlue', caps='Gray')
    dataHumidity.plot.box(color=color, sym='r+')

    # Labeling the graphs
    title = "Boxplot of humidity in a week"
    plt.title(title)
    plt.xlabel('')
    plt.ylabel('Humidity')

    # Save graph to a file called "boxplot.png"
    dirPath = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots\\Humidity"
    dirPathFile = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots\\Humidity\\boxplot"

    # initialize directory if it doesn't exist
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)

    plt.savefig(dirPathFile + ".png")


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def plotGraph():
    # Humidity against date
    # print 'Plotting humidity graphs...'
    # lineGraphHumidity()  # line graph
    # boxPlotHumidity()  # box plot

    #TODO: bug: linegraph gets a boxplot instead

    # Temperature against date
    print 'Plotting temperature graphs...'
    lineGraphTemp()  # line graph
    boxPlotTemp()  # box plot

    dirPath = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots"
    print '\nGraphs saved in ' + dirPath

# -=-= Run the functions to obtain plots -=-=
plotGraph()


# From python shell, type:
# execfile("MeetingRoom1.py")
