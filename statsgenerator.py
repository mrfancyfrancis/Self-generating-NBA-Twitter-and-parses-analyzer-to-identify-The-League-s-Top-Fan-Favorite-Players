#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 23:44:41 2019

@author: FranChan
"""

import csv
nba = []
players = []
stats = []
with open('nba.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            nba.append(row)
            players.append("")
        else:
            nba.append([row[0],float(row[1])])
            players.append(row[0])
        line_count += 1
with open('nbaplayers1718.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 1
    for row in csv_reader:
        if line_count == 0:
            print(row)
        else:
            if row[2] in players:
                g = float(row[7])
                #points
                ppg = float(row[53])/g
                nba[players.index(row[2])].append(ppg)
                #assist
                apg = float(row[48])/g
                nba[players.index(row[2])].append(apg)
                #rebounds
                rpg = float(row[47])/g
                nba[players.index(row[2])].append(rpg)
                #steals
                spg = float(row[49])/g
                nba[players.index(row[2])].append(spg)
                #blocks
                bpg = float(row[50])/g
                nba[players.index(row[2])].append(bpg)
                #PER
                nba[players.index(row[2])].append(float(row[10]))
        line_count += 1
    print(f'Processed {line_count} lines.')
with open('nba.csv', mode='w') as csv_file:
    csv_file = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in nba:
        csv_file.writerow(i)
        