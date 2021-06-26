import numpy as np
'''
gather all of the tiles on the board and in your hand
count them up 0 to 2 for each tile, recorded in y array
y array:
y[0:13] corresponds to Red tiles
y[13:26] corresponds to Blue tiles
y[26:39] corresponds to Yellow tiles
y[39:52] corresponds to Black tiles
y[52] corresponds to Joker

Ex: with hand R2 J0 Y8 K3 Y8 K6
y[1] = 1. y[33] = 2, y[41] = 1, y[44] = 1, y[52] = 1
all other y indices are 0


'''
tileToIndex = []
for i in ['R','B','Y','K']:
    for j in range(13):
        tileToIndex.append(i+str(j+1))
tileToIndex.append('J0')
tileToIndex = tuple(tileToIndex)


