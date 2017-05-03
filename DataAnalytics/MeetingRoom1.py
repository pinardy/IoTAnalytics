import matplotlib.pyplot as plt
import pandas as pd
import os

# Meeting room 1, sensor 1

# "header = 0" means '0' index is the header
# "parse_dates=[0]" converts the Strings under the first column into datetime64 objects

plt.style.use('ggplot')
data = pd.read_csv("datasets\\Temperature- Meeting Room 1 - Sensor 1.csv",
                 parse_dates=[0], header=0, usecols=[0, 1])


# -=-=-=-=-= PRINTING OF DATA -=-=-=-=-=
# print data
# print data['Date & Time']
# print data['Value']
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


def plotGraph():
    plt.plot(data['Date & Time'], data['Value'], '*')
    plt.xticks(rotation='vertical')

    # Labeling the graphs
    title = "Date against Temperature"
    plt.title(title)
    plt.xlabel('Date & Time')
    plt.ylabel('Temperature')

    # Save graph to a file called "graph.png"
    dirPath = os.path.dirname(os.path.realpath(__file__)) + "\\graph"
    plt.savefig(dirPath + ".png")

plotGraph()

# From python shell, type:
# execfile("MeetingRoom1.py")