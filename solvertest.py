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
# list(combinations(no_dupe,3)) +  + list(combinations(no_dupe,5))
comb = list(combinations(no_dupe,4))
comb_clean = []
for i in comb:
    try:
        comb_clean.append([x.string for x in group(i).group])
    except:
        pass

print(*[x for x in comb_clean],sep='\n')
print(len(comb_clean))