from itertools import combinations
from group import group
from tile import tile
def generateNoJokerSet(highestNum, colors):
    noJokerSet = []
    for color in colors:
        for i in range(3, highestNum + 1):
            noJokerSet.append(group([tile(i-2, color), tile(i-1, color), tile(i, color)]))
            if i > 3:
                noJokerSet.append(group([tile(i-3, color), tile(i-2, color), tile(i-1, color), tile(i, color)]))
            if i > 4:
                noJokerSet.append(group([tile(i-4, color), tile(i-3, color), tile(i-2, color), tile(i-1, color), tile(i, color)]))
    
    colorCombinationsList = []
    for i in range(3, len(colors)):
        colorCombinations = list(combinations(colors, i))
        colorCombinationsList.append(colorCombinations)
    for i in range(1, highestNum + 1):
        for colorList in colorCombinationsList:
            for colorcombinations in colorList:
                tempGroup = []
                for color in colorcombinations:
                    tempGroup.append(tile(i, color))
                noJokerSet.append(group(tempGroup))

    return noJokerSet

def generateOneJokerSet(noJokerSet):
    oneJokerSet = []
    for party in noJokerSet:
        for i in range(0, len(party.group)):
            partyCopy = party.group[:]
            partyCopy[i] = tile(0, 'J')
            oneJokerSet.append(partyCopy)
    return oneJokerSet

def generateTwoJokerSet(oneJokerSet):
    twoJokerSet = []
    for party in oneJokerSet:
        for i in range(0, len(party)):
            if party[i].color != 'J':
                partyCopy = party[:]
                partyCopy[i] = tile(0, 'J')
                twoJokerSet.append(partyCopy)
    return twoJokerSet

def generateSet(highestNum, colors):

    bigSet = generateNoJokerSet(highestNum, colors)
    oneJokerSet = generateOneJokerSet(bigSet)
    bigSet.extend(oneJokerSet)
    twoJokerSet = generateTwoJokerSet(oneJokerSet)
    bigSet.extend(twoJokerSet)
    return bigSet

print(len(generateSet(13,['R','B','K','Y'])))