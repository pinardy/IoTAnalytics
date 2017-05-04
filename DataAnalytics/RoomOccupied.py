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
inputFileTemp = "datasets\\mtgrm1_s1\\Temperature (24-28 Apr)- Meeting Room 1 - Sensor 1.csv"

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

# print (dataMotion['Date & Time'].eq(dataTemp['Date & Time'], axis=0))
print dataMotion
print dataTemp

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
    # Motion against date
    print '\nPlotting motion graphs...'
    motionGraph()  # line graph

    dirPath = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots"
    print 'Graphs saved in ' + dirPath



# -=-= Run the functions to obtain plots -=-=
# plotGraph()