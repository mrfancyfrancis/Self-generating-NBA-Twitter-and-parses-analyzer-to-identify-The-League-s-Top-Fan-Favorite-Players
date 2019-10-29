#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 00:44:31 2019

@author: FranChan
"""
import csv
from random import choice
from functools import reduce # only in Python 3
def Dict(**args): 
    """Return a dictionary with argument names as the keys, 
    and argument values as the key values"""
    return args
nba = []
players = []
totaltweets = 0
with open('nba.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    i = 0
    for row in csv_reader:
        if i == 0:
            nba.append(row)
        else:
            nba.append([row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),int(row[5]),int(row[6]),int(row[7])])
            totaltweets+=int(row[1])
            players.append(row[0])
        i+=1

grammar = Dict(
        S = [['NP','VP','H'],['NP','VP','H','H'],['NP','VP','H','H','H']],
        NP = [['N'], ['N', 'PP']],
        VP = [['V','A', 'Q','NP'], ['V', 'PV'],['AV','Det','A','VN']],
        PP = [['P', 'N']],
        PV = [['AE'],['AE','PP']],
        Det = ['the', 'a'],
        Q = ['on','at','above'],
        P = ['with','against'],
        J = ['red', 'big'],
        N = players,
        V = ['play', 'shoot', 'dunk', 'score', 'pass', 'steal', 'defend'],
        VN = ['player', 'shooter', 'dunker', 'scorer', 'passer', 'stealer', 'defender'],
        AV = ['is',"isn't"],
        A = ['good','bad','great','worse'],
        AE = ['nicely','badly','horribly','wildly','elegantly'],
        H = ['#NBA','#NBAAllStar','#NBAPlayoffs','#basketball','#ballislife','#mvp','#nbabasketball']
        )

def generate(phrase):
    "Generate a random sentence or phrase"
    if isinstance(phrase, list): 
        return mappend(generate, phrase)
    elif phrase in grammar:
        return generate(choice(grammar[phrase]))
    else: return [phrase]
def mappend(fn, list):
    "Append the results of calling fn on each element of list."
    return reduce(lambda x,y: x+y, map(fn, list))
tweets = []
nba.pop(0)
for i in nba:
    sc = 0
    while sc < i[1]:
        s = generate('S')
        if s[0] == i[0]:
            sc+=1
            tweets.append(" ".join(s))
for t in tweets:
    print(t)
with open('tweets.txt', 'w') as f:
    for item in tweets:
        f.write("%s\n" % item)