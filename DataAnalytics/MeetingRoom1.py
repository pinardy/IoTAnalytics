import matplotlib.pyplot as plt
import pandas as pd
import os

# -=-=-= Meeting room 1, sensor 1 -=-=-=

'''
----- DataFrame objects -----
"header = 0" means '0' index is the header
"parse_dates=[0]" converts the Strings under the first column into datetime64 objects
'''

# input files
inputFileTemp = "datasets\\Temperature (24-28 Apr)- Meeting Room 1 - Sensor 1.csv"
inputFileHumidity = "datasets\\Humidity (24-28 Apr)- Meeting Room 1 - Sensor 1.csv"

# create DataFrame objects
dataTemp = pd.read_csv(inputFileTemp,
                       parse_dates=[0], header=0, usecols=[0, 1])
dataHumidity = pd.read_csv(inputFileHumidity,
                           parse_dates=[0], header=0, usecols=[0, 1])

# Converts date/time data to datetime64 object
dataTemp['Date & Time'] = pd.to_datetime(dataTemp['Date & Time'])

#TODO: find out what happened to the 'Date & Time' key
# dataTemp = dataTemp.set_index(keys='Date & Time', inplace=False, append=True, drop=True)

dataTemp = dataTemp.set_index('Date & Time')
# print dataTemp.keys()
# print '\nIndex:', type(dataTemp.index)

# Set time frame from 9am to 6pm
dataTemp = dataTemp.between_time('9:00', '18:00')

# Reset index so that we can plot the graph later
dataTemp.reset_index(inplace = True)
# print '\nIndex:', type(dataTemp.index)

# print dataTemp.keys()



# -=-=-=-=-= PRINTING OF DATA -=-=-=-=-=
# print dataTemp['Date & Time']
# print dataTemp['Value']
print dataTemp
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


# -=-=-=-=-= TEMPERATURE -=-=-=-=-=

def lineGraphTemp():
    plt.plot(dataTemp['Date & Time'], dataTemp['Value'], linestyle='-', color='b')
    plt.xticks(rotation='vertical')

    # Labeling the graphs
    title = "Temperature against Date"
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Temperature')

    # displays graph
    plt.show()

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

    # displays graph
    plt.show()

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

    # displays graph
    plt.show()

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

    # displays graph
    plt.show()

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

    #TODO: bug: linegraph gets a boxplot instead (plot temp & humidity separately first)

    # Temperature against date
    print '\nPlotting temperature graphs...'
    lineGraphTemp()  # line graph
    boxPlotTemp()  # box plot

    dirPath = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots"
    print 'Graphs saved in ' + dirPath

# -=-= Run the functions to obtain plots -=-=
plotGraph()

# From python shell, type:
# execfile("MeetingRoom1.py")
