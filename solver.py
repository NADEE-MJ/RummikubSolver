import numpy as np
import ILP

def checkLen(elem):
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




    groupsFromHand = np.where(xarray==1)
    makeableGroups = 2*list(np.array(exhaustiveList)[groupsFromHand])
    makeableGroups.sort(key=checkLen,reverse=True)
    for item in makeableGroups:
        print(*[x.string for x in item.group])





    bestLen = 0
    bestChoice = []
    for i in range(len(makeableGroups)):
        # handCopy = exampleHand.hand[:]
        # handCopyStrings = [x.string for x in handCopy]
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
            bestPlay = masterStrings[:]
                
    
    for item in bestChoice:
        print([x.string for x in item])
