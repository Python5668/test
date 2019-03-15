### Homework 18
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('data_tasks.xlsx', sheet_name = 'task1')
time = df.values[:,0]
temp = df.values[:,1]
std = df.values[:,2]

## Line Plot
#line, caps, bars = plt.errorbar([time], [temp], yerr = [std], fmt = 'bs--',
#                                linewidth = 3, elinewidth = 2,
#                                ecolor = 'k', capsize = 4, capthick = 1)
#plt.xlabel('Time Point (minute)', fontsize = 14)
#plt.ylabel('Tempurature (C)', fontsize = 14)
#plt.yticks(np.arange(6,24,2), fontsize = 14)
#plt.xticks(fontsize = 14)
#plt.title("Task 1 Line Plot", fontsize = 24)
#plt.legend(["Standard Deviation"], numpoints = 1, loc = "upper right",
#           fontsize = 16)
#plt.savefig('Task1.jpg', dpi = 600)
#plt.show()

## Bar Plot
#plt.bar(time, temp, color = "green", yerr = std, capsize = 9,width = 0.7)
#plt.xlabel('Time Point (minute)', fontsize = 14)
#plt.ylabel('Tempurature (C)', fontsize = 14)
#plt.yticks(np.arange(0,24,2), fontsize = 14)
#plt.xticks([1,2,3,4,5,6,7,8,9],fontsize = 14)
#plt.title("Task 1 Bar Plot", fontsize = 20)  
#plt.show()

af = pd.read_excel('data_tasks.xlsx', sheet_name = 'task2')
time = af.values[1:,0]
std = af.values[1:,2]
VTemp = af.values[1:,1]
DuTemp = af.values[1:,3]
DeTemp = af.values[1:,5]

## Line Plot
#plt.grid(which = 'major', axis = 'both')
#line, caps, bars = plt.errorbar([time],[VTemp], fmt = 'gs--', yerr = [std],
#                                capsize = 9, linewidth = 3, ecolor = 'k')
#
#line, caps, bars = plt.errorbar([time],[DuTemp], fmt = 'rs--', yerr = [std],
#                                capsize = 9, linewidth = 3, ecolor = 'r')
#
#line, caps, bars = plt.errorbar([time],[DeTemp], fmt = 'bs--', yerr = [std],
#                                capsize = 9, linewidth = 3, ecolor = 'k')
#
#plt.xlabel('Time Point (Hour)', fontsize = 14)
#plt.ylabel('Tempurature (C)', fontsize = 14)
#plt.title('Task 2 Line Plot', fontsize = 20)
#plt.yticks(np.arange(2,56,4),fontsize = 14)
#plt.xticks(fontsize = 14)
#plt.legend(['Las Vegas','Durango','Denver'], fontsize = 14)
#plt.show()

## Bar Plot
#plt.bar(time-0.25, VTemp, color = '#7f6d5f', width = 0.25, edgecolor = 'white',
#        label = 'Las Vegas', yerr = std, capsize = 6)
#
#plt.bar(time, DuTemp, color = '#557f2d', width = 0.25, edgecolor = 'white',
#        label = 'Durango', yerr = std, capsize = 6)
#
#plt.bar(time+0.25, DeTemp, color = '#2d7f5e', width = 0.25, edgecolor = 'white',
#        label = 'Denver', yerr = std, capsize = 6)
#
#plt.xlabel('Time Point (Hour)', fontsize = 14)
#plt.ylabel('Tempurature (C)', fontsize = 14)
#plt.title('Task 2 Bar Plot', fontsize = 20)
#plt.yticks(np.arange(2,56,4),fontsize = 14)
#plt.xticks(np.arange(1,7),fontsize = 14)
#plt.legend(['Las Vegas','Durango','Denver'], fontsize = 14)
#plt.show()