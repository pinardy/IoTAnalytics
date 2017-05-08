import matplotlib.pyplot as plt
import pandas as pd
import os

# -=-=-= Extract data out from CSV file (either 24 hours or working hours) -=-=-=

'''
----- DataFrame objects -----
"header = 0" means '0' index is the header
"parse_dates=[0]" converts the Strings under the first column into datetime64 objects
'''

# input files
inputFileTemp = "datasets\\mtgrm1_s1\\Temperature (24-28 Apr)- Meeting Room 1 - Sensor 1.csv"
inputFileHumidity = "datasets\\mtgrm1_s2\\Humidity (24-28 Apr)- Meeting Room 1 - Sensor 2.csv"
inputFileMotion = "datasets\\mtgrm1_s1\\Motion (24-28 Apr)- Meeting Room 1 - Motion Sensor 1.csv"

# create DataFrame objects
dataTemp = pd.read_csv(inputFileTemp,
                       parse_dates=[0], header=0, usecols=[0, 1])
dataHumidity = pd.read_csv(inputFileHumidity,
                           parse_dates=[0], header=0, usecols=[0, 1])
dataMotion = pd.read_csv(inputFileMotion,
                           parse_dates=[0], header=0, usecols=[0, 1])

## Converts date/time data to datetime64 object
dataTemp['Date & Time'] = pd.to_datetime(dataTemp['Date & Time'])
dataHumidity['Date & Time'] = pd.to_datetime(dataHumidity['Date & Time'])
dataMotion['Date & Time'] = pd.to_datetime(dataMotion['Date & Time'])

dataTemp = dataTemp.set_index('Date & Time')
dataHumidity = dataHumidity.set_index('Date & Time')
dataMotion = dataMotion.set_index('Date & Time')

## Set time frame from 9am to 6pm
# dataTemp = dataTemp.between_time('9:00', '18:00')
dataHumidity = dataHumidity.between_time('9:00', '18:00')
dataMotion = dataMotion.between_time('9:00', '18:00')

## Reset index so that we can plot the graph later
dataTemp.reset_index(inplace = True)
dataHumidity.reset_index(inplace = True)
dataMotion.reset_index(inplace = True)


# -=-=-=-=-= PRINTING OF DATA -=-=-=-=-=
# print dataTemp['Date & Time']
# print dataTemp['Value']
# print dataTemp
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


# -=-=-=-=-= TEMPERATURE -=-=-=-=-=

def lineGraphTemp():
    plt.plot(dataTemp['Date & Time'], dataTemp['Value'], linestyle='-', color='b')
    plt.xticks(rotation='vertical')

    # Labeling the graphs
    plt.title("Temperature against Date")
    plt.xlabel('Date')
    plt.ylabel('Temperature ($^\circ$C)')

    # Now add the legend with some customizations.
    # plt.legend(loc='upper center', shadow=True)

    ## Widen the width of graph
    # dataTemp.plot(figsize=(15, 4))

    # displays graph
    # plt.show()

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
    plt.xticks([]) # hides the default 'Value' label on x-axis
    plt.ylabel('Temperature ($^\circ$C)')

    # displays graph
    # plt.show()

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
    # plt.show()

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
    # plt.show()

    # Save graph to a file called "boxplot.png"
    dirPath = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots\\Humidity"
    dirPathFile = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots\\Humidity\\boxplot"

    # initialize directory if it doesn't exist
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)

    plt.savefig(dirPathFile + ".png")

# -=-=-=-=-= MOTION -=-=-=-=-=

def motionGraph():
    plt.plot(dataMotion['Date & Time'], dataMotion['Value'], linestyle='-', color='b')
    plt.xticks(rotation='vertical')

    # Labeling the graphs
    title = "Motion against Date"
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Motion')

    # displays graph
    # plt.show()

    # Save graph to a file called "graph.png"
    dirPath = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots\\Motion"
    dirPathFile = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots\\Motion\\motiongraph"

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

    # Temperature against date
    print '\nPlotting temperature graphs...'
    lineGraphTemp()  # line graph
    boxPlotTemp()  # box plot

    # Motion against date
    # print '\nPlotting motion graphs...'
    # motionGraph()  # line graph

    dirPath = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots"
    print 'Graphs saved in ' + dirPath

# -=-= Run the functions to obtain plots -=-=
plotGraph()

# From python shell, type:
# execfile("ExtractData.py")
