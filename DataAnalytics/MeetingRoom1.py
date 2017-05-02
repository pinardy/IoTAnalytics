import matplotlib.pyplot as plt
import pandas as pd

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

plt.plot(data['Date & Time'], data['Value'], '*')
plt.xticks(rotation='vertical')

# From python shell, type:
# execfile("MeetingRoom1.py")