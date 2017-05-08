import matplotlib.pyplot as plt
import pandas as pd
import os

# -=-=-= Extract data out from CSV file (either 24 hours or working hours) -=-=-=

'''
----- DataFrame objects -----
"header = 0" means '0' index is the header
"parse_dates=[0]" converts the Strings under the first column into datetime64 objects
'''

# input file
inputFileMotion = "datasets\\mtgrm1_s1\\Motion (24-28 Apr)- Meeting Room 1 - Motion Sensor 1.csv"
inputFileTemp = "datasets\\mtgrm1_AC\\Temperature (24-28 Apr)- Meeting Room 1 - AC Controller.csv"

# create DataFrame objects
dataMotion = pd.read_csv(inputFileMotion,
                           parse_dates=[0], header=0, usecols=[0, 1])
dataTemp = pd.read_csv(inputFileTemp,
                       parse_dates=[0], header=0, usecols=[0, 1])

## Converts date/time data to datetime64 object
dataMotion['Date & Time'] = pd.to_datetime(dataMotion['Date & Time'])
dataTemp['Date & Time'] = pd.to_datetime(dataTemp['Date & Time'])

dataMotion = dataMotion.set_index('Date & Time')
dataTemp = dataTemp.set_index('Date & Time')

## Set time frame from 9am to 6pm
dataTemp = dataTemp.between_time('9:00', '18:00')
dataMotion = dataMotion.between_time('9:00', '18:00')

## Reset index so that we can plot the graph later
dataMotion.reset_index(inplace = True)
dataTemp.reset_index(inplace = True)

# Only extract data for which there is motion
dataMotion = dataMotion.loc[dataMotion['Value'] == 1]

# -=-=-=-=-= PRINTING OF DATA -=-=-=-=-=
# print (dataMotion['Date & Time'].eq(dataTemp['Date & Time'], axis=0))
# print dataMotion['Date & Time'].describe()
# print dataTemp['Date & Time'].describe()
# print dataMotion
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


''' Iterate over every element in column and get difference.
  If difference in time is small enough (5 mins), we take that row of data
  PURPOSE: obtain index of rows where the times of the 2 data being compared are close enough
'''
indexList = []
def iterateData(data1, data2):
    indexTemp = 0
    indexMotion = 0
    timeBoundary = pd.Timedelta('0 days 00:05:00') # for checking if the data is within 15 mins of each other
    timeFloor = pd.Timedelta('0 days 00:00:00') # we want the difference to be positive

    for timeStamp in data1['Date & Time']:
        indexTemp += 1
        for timeStamp2 in data2['Date & Time']:
            indexMotion += 1
            if (timeFloor < (timeStamp - timeStamp2) and (timeStamp - timeStamp2) < timeBoundary):
                # add index to a list
                indexList.append(indexTemp)


# print dataTemp['Date & Time'].size  # 465
# print dataMotion['Date & Time'].size  # 34

iterateData(dataTemp, dataMotion)
filteredData = dataTemp.ix[indexList] # match indexList to dataTemp
# print indexList
print filteredData

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


# -=-=-=-=-= TEMPERATURE -=-=-=-=-=

def tempGraph():
    plt.plot(filteredData['Date & Time'], filteredData['Value'], linestyle='-', color='b')
    plt.xticks(rotation='vertical')

    # Labeling the graphs
    plt.title("Temperature against Date (Activity only)")
    plt.xlabel('Date')
    plt.ylabel('Temperature ($^\circ$C)')

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
    filteredData.plot.box()
    color = dict(boxes='DarkGreen', whiskers='DarkOrange',
                 medians='DarkBlue', caps='Gray')
    filteredData.plot.box(color=color, sym='r+')

    # Labeling the graphs
    title = "Boxplot of temperature in a week"
    plt.title(title)
    plt.xlabel('')
    plt.ylabel('Temperature ($^\circ$C)')

    # displays graph
    # plt.show()

    # Save graph to a file called "boxplot.png"
    dirPath = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots\\Temperature"
    dirPathFile = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots\\Temperature\\boxplot_activity"

    # initialize directory if it doesn't exist
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)

    plt.savefig(dirPathFile + ".png")

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def plotGraph():
    # Motion against date
    # print '\nPlotting motion graphs...'
    # motionGraph()  # line graph

    # Temperature against date (Activity only)
    print '\nPlotting temperature graphs...'
    tempGraph()  # line graph
    boxPlotTemp() # box plot

    dirPath = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots"
    print 'Graphs saved in ' + dirPath



# -=-= Run the function to obtain plots -=-=
plotGraph()