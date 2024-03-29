import matplotlib.pyplot as plt
import pandas as pd
import os

'''
--- Climate of Singapore ---
Period: March/April
Station: Ang Mo Kio
Data: Daily
'''

# index 3: day, index 8: mean temp
dataTemp = pd.read_csv("datasets\\climate_april_SG.csv",
                       header=0, usecols=[3, 8])

# select days 15 - 31
dataTemp = dataTemp[14:31]

# print dataTemp.corr()
# print dataTemp
# print dataTemp.describe()

def lineGraphTemp():
    plt.plot(dataTemp['Day'], dataTemp['Mean Temperature'], linestyle='-', color='b')
    plt.xticks(rotation='vertical')

    # Labeling the graphs
    title = "Mean temperature against Day (April)"
    plt.title(title)
    plt.xlabel('Day')
    plt.ylabel('Mean temperature ($^\circ$C)')

    # Save graph to a file called "graph.png"
    dirPath = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots\\Temperature"
    dirPathFile = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots\\Temperature\\sg_april_linegraph"

    # initialize directory if it doesn't exist
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)

    plt.savefig(dirPathFile + ".png")

def plotGraph():
    # Temperature against date
    print '\nPlotting temperature graph...'
    lineGraphTemp()
    dirPath = os.path.dirname(os.path.realpath(__file__)) + "\\dataplots"
    print 'Graph saved in ' + dirPath

plotGraph()