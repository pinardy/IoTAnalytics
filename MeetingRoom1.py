import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

# Meeting room 1, sensor 1

plt.style.use('ggplot')
data = pd.read_csv("datasets\\Temperature- Meeting Room 1 - Sensor 1.csv",
                 parse_dates=[0], header=None, usecols=[0, 1])

# print type(data) # pandas.core.frame.DataFrame
print data
