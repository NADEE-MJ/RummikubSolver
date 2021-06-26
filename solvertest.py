import numpy as np
from group import UniqueColorError, group
from tile import tile
from drawpile import drawPile
from itertools import combinations
# y is 1-13 for all 4 colors(RBYK), +1 for joker
# each value can be 0,1,2
y = np.zeros(53)
print(y)

d=drawPile()
d.drawPile=[]
d.createPile()
slicee = d.drawPile[:]
no_dupe = []
no_dupe_string = []
for i in d.drawPile:
    if i.cstring not in no_dupe_string:
        no_dupe.append(i)
        no_dupe_string.append(i.cstring)

no_dupe.append(d.drawPile[-1])
# print(*no_dupe_string)

# valid3 = []
# for i in no_dupe:
#     temp1 = no_dupe[:]
#     temp1.remove(i)
#     for j in temp1:
#         temp2 = temp1[:]
#         temp2.remove(j)
#         for k in temp2:
#             try:
#                 valid3.append([x.string for x in group([i,j,k]).group])
#             except:
#                 pass

# print(*valid3,sep='\n')
# print(len(valid3))

comb = list(combinations(no_dupe,3)) + list(combinations(no_dupe,4)) + list(combinations(no_dupe,5))
comb_clean = []
for i in comb:
    try:
        comb_clean.append([x.string for x in group(i).group])
    except:
        pass

print(*[x for x in comb_clean],sep='\n')
print(len(comb_clean))
'''
1 2 3       1 2 J   1 J 3   J 2 3
2 3 4       #2 3 J   2 J 4   J 3 4
3 4 5       #3 4 J   3 J 5   J 4 5
4 5 6       #4 5 J   4 J 6   J 5 6
5 6 7       #5 6 J   5 J 7   J 6 7
6 7 8       #6 7 J   6 J 8   J 7 8
7 8 9       #7 8 J   7 J 9   J 8 9
8 9 10      #8 9 J   8 J 10  J 9 10
9 10 11     #9 10 J  9 J 11  J 10 11
10 11 12    #10 11 J 10 J 12 J 11 12
11 12 13    #11 12 J 11 J 13 J 12 13
'''