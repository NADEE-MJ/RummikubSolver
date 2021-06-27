from drawpile import drawPile
import numpy as np
import ILP
from hand import hand
'''
gather all of the tiles on the board and in your hand
count them up 0 to 2 for each tile, recorded in y array
y[i] array:
y[0:13] corresponds to Red tiles
y[13:26] corresponds to Blue tiles
y[26:39] corresponds to Yellow tiles
y[39:52] corresponds to Black tiles
y[52] corresponds to Joker

Ex: with hand R2 J0 Y8 K3 Y8 K6
y[1] = 1. y[33] = 2, y[41] = 1, y[44] = 1, y[52] = 1
all other y indices are 0

x[j] array:
as long as the total number of every possible group in the game
at each index is a 0,1, or 2
indicates how many times that group can be played based on hand+board

s[i][j] matrix:
each location i,j has 1 if tile i is in set j
0 if tile i not in set j

r[i] array:
tiles on your rack, same format as y[i]
y[i] <= r[i]
y[i] is tiles from rack that can be played, so if y[i] == r[i], you win

t[i] array:
tiles on the table, same format as y[i]

The hard part:
Maximize Sum of y[i] over all i∈{1,2...,53}
subject to: Sum of s[i][j]x[j] == t[i] + y[i]
            y[i] <= r[i]
            x[j] ∈ {0,1,2}
            y[j] ∈ {0,1,2}

source: doi:10.1093/comjnl/bxl033
'''
# tileToIndex = []
# for i in ['R','B','Y','K']:
#     for j in range(13):
#         tileToIndex.append(i+str(j+1))
# tileToIndex.append('J0')
# tileToIndex = tuple(tileToIndex)

exampleDraw = drawPile()
exampleHand = hand(exampleDraw,1)

exHandStrings = [x.string for x in exampleHand.hand]

exhaustiveList = ILP.generateSet(13,['R','B','K','Y'])
xarray = np.zeros(len(exhaustiveList))
for item in exhaustiveList:
    jokerCount = 0
    tileCounter = 0
    for el in item.group:
        if el.string in exHandStrings:
            tileCounter += 1
            if el.string == 'J0':
                exHandStrings.remove('J0')
                jokerCount += 1
    if tileCounter == len(item.group):
        xarray[exhaustiveList.index(item)] += 1
    exHandStrings.extend(jokerCount*['J0'])

print(exHandStrings)
print(xarray)
# print(exhaustiveList)



