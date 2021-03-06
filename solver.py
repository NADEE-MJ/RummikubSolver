import numpy as np
from group import group
import combGen

def checkLen(elem):
    """
    (group) -> int

    returns the length of a group
    """
    return len(elem.group)

def solver(currHand, currBoard):
    """
    ([tile], [group]) -> ([group], [tile])

    Takes in the current hand and current board then creates a 
    exhaustive list of all the possibilities for a group in rummikub.
    Finds the possible groups that can be made with the current hand 
    and board. Then checks all possible combinations of possible groups
    to find the set of groups that contains the most tiles
    """
    boardCopy = []
    for item in currBoard:
        boardCopy.extend(item.group)

    exHand = currHand + boardCopy
    exHandStrings = [x.string for x in exHand]

    # this is a list of every possible unique group
    # xarray is the location of all groups that can be made from the tiles in the masterList
    exhaustiveList = combGen.generateSet(13,['R','B','K','Y'])
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

    # makeablegroups is a list with all of the groups that can be made from the masterList
    # the list has duplicates of everything to account for the presence of 2 of each tile in the game
    groupsFromHand = np.where(xarray==1)
    makeableGroups = 2*list(np.array(exhaustiveList)[groupsFromHand])
    makeableGroups.sort(key=checkLen,reverse=True)

    # this algorithm goes through each group and the following groups and determines the best
    # set of groups to play to maximize the total number of tiles played
    bestPlay = []
    bestLen = 0
    bestChoice = []
    for i in range(len(makeableGroups)):
        boardCopy = []
        for item in currBoard:
            boardCopy.extend(item.group)
        boardCopyStrings = [x.string for x in boardCopy]
        
        masterList = exHand[:]
        masterStrings = [x.string for x in masterList]

        useThese = []
        for item in makeableGroups[i:]:
            tempGroup = []
            for el in item.group:
                try:
                    masterList.pop(masterStrings.index(el.string))
                    masterStrings.remove(el.string)
                except:
                    masterList.extend(tempGroup)
                    masterStrings.extend([x.string for x in tempGroup])
                    tempGroup = []
                    break
                tempGroup.append(el)

            if tempGroup != []:
                useThese.append(tempGroup)
        
        newsThese = []
        for i in useThese:
            newsThese.extend(i)
        useTheseStrings = [x.string for x in newsThese]
        boardCheck = True
        for el in boardCopyStrings:
            if el in useTheseStrings:
                useTheseStrings.remove(el)
            else:
                boardCheck = False
                break
        
        if boardCheck and bestLen < len(newsThese):
            bestChoice = useThese[:]
            bestLen = len(newsThese)
            bestPlay = masterList[:]

    # converts list of lists to list of groups
    groupsToAdd = []
    for currGroup in bestChoice:
        groupsToAdd.append(group(currGroup))
    
    if len(groupsToAdd) == 0:
        return None, bestPlay

    return groupsToAdd, bestPlay