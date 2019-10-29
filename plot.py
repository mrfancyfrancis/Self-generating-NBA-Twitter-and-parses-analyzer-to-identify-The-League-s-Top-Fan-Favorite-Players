#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 01:53:16 2019

@author: FranChan
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import csv
from copy import deepcopy
limit = int(input("Enter a limit from 1-75: "))
popularity = [[],[]]
with open('nba.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    i = 0
    for row in csv_reader:
        if i != 0:
            #popularity.append([row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),int(row[5]),int(row[6]),int(row[7])])
            popularity[0].append(row[0])
            popularity[1].append(int(row[1]))
        i+=1

objects = popularity[0][:limit]
y_pos = np.arange(len(objects))
performance = popularity[1][:limit]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Popularity')
plt.title('NBA Players by Popularity based on tweets')

plt.show()
likability = [[],[],[]]
with open('popularity.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    i = 0
    for row in csv_reader:
        if i != 0:
            #popularity.append([row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),int(row[5]),int(row[6]),int(row[7])])
            likability[0].append(row[0])
            likability[1].append(int(row[1]))
            likability[2].append(int(row[2]))
        i+=1

fig, ax = plt.subplots()
ax.scatter(likability[2][:limit], likability[1][:limit])
plt.title("NBA Player's Likeability by Popularity")
plt.xlabel("Likeability")
plt.ylabel("Popularity")
for i, txt in enumerate(likability[0][:limit]):
    ax.annotate(txt, (likability[2][i], likability[1][i]))
#for i, txt in enumerate(n):
#    ax.annotate(txt, (z[i], y[i]))
    
performance = deepcopy(likability)
performance.pop(1)
performance.append([])
with open('nba.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    i = 0
    for row in csv_reader:
        if i != 0:
            #popularity.append([row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),int(row[5]),int(row[6]),int(row[7])])
            performance[2].append(int(row[7]))
        i+=1
fig, bx = plt.subplots()
bx.scatter(performance[1][:limit], performance[2][:limit])
plt.title("NBA Players. Performance by Likeability")
plt.xlabel("Performance")
plt.ylabel("Likeability")
for i, txt in enumerate(performance[0][:limit]):
    bx.annotate(txt, (performance[1][i], performance[2][i]))