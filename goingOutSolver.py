from tile import tile
from group import GroupError, InvalidJokerError, RunError, SetError, UniqueColorError, group

def takeSecond(elem):
    """
    ([]) -> [][1]
    
    returns the second element of a list
    """
    return elem[1]

def goingOutSolver(solverHand):
    """
    ([tile]) -> ([group], [tile]) or (None, None)

    Given a list of tiles in a hand this function check to see if there is any possible
    way for the player to use this hand to go out with requires enough sets and
    runs to add up to 30 points
    """
    #converts solverHand from [tile] to [[int, char]]
    currHand = []
    jokerCount = 0
    for currTile in solverHand:
        currHand.append([currTile.value, currTile.color])
        if currTile.value == 0:
            jokerCount += 1
    
    #orders currHand by value descending and checks for valid sets not including jokers
    currHand.sort(reverse=True)
    
    tempOutGroups, currHand = setCheck(currHand)

    #orders currhand by value descending and then by color
    currHand.sort(reverse=True)
    currHand.sort(key=takeSecond)

    #checks for runs not including jokers
    tempList, currHand = runCheck(currHand)
    tempOutGroups.extend(tempList)

    #converts tempOutGroups to format = [group] and determines tiles to remove
    outGroups, tilesToRemove = convertToListOfGroups(tempOutGroups)

    #caculates value of OutGroups
    outGroupsValue = calculateOutGroupsValue(outGroups)

    #check if outGroups is worth 30 points
    if outGroupsValue >= 30:
        return outGroups, tilesToRemove
    else:
        print("Not able to go out.")
        return None, None

def setCheck(currHand):
    """
    ([[int, char]]) -> ([group], [[int, char]])

    Checks if given a hand can you create any sets based off the rules of a set in
    rummikub, must all be the same number but all different colors.
    """
    prevTile = 0
    tempGroup = []
    tempOutGroups = []
    addedColors = []
    for currTile in currHand:
        if currTile[0] == prevTile and currTile[1] not in addedColors and len(tempGroup) < 5:
            tempGroup.append(currTile)
            addedColors.append(currTile[1])
            if len(tempGroup) == 4:
                tempOutGroups.append(tempGroup)
                for tileToRemove in tempGroup:
                    currHand.remove(tileToRemove)
                prevTile = 0
                tempGroup = []
                addedColors = []
        else:
            if len(tempGroup) >= 3:
                tempOutGroups.append(tempGroup)
                for tileToRemove in tempGroup:
                    currHand.remove(tileToRemove)
            prevTile = currTile[0]
            tempGroup = []
            addedColors = []
            tempGroup.append(currTile)
            addedColors.append(currTile[1])

    return tempOutGroups, currHand

def runCheck(currHand):
    """
    ([[int, char]]) -> ([group], [[int, char]])

    Checks if given a hand can you create any runs based off the rules of a run in
    rummikub, must be in increasing order and all the same color.
    """
    #checks for runs
    prevTile = 0
    tempGroup = []
    tempOutGroups =[]
    currColor = ''
    
    for currTile in currHand:
        if currTile[0] < prevTile and currTile[1] == currColor:
            tempGroup.append(currTile)
            prevTile = currTile[0]
        elif currTile[0] == prevTile and currTile[1] == currColor:
            continue
        else:
            if len(tempGroup) >= 3:
                tempOutGroups.append(tempGroup)
                for tileToRemove in tempGroup:
                    currHand.remove(tileToRemove)
            tempGroup = []
            prevTile = currTile[0]
            currColor = currTile[1]
    
    return tempOutGroups, currHand

def convertToListOfGroups(tempOutGroups):
    """
    ([[[int, char]]]) -> ([group], [tile])

    Converts [[[int, char]]] to [group] and determines which tiles need to be removed
    from the players hand a returns a [tile] of tiles that need to be removed.
    """
    tempGroup = []
    tilesToRemove = []
    outGroups = []
    for currGroup in tempOutGroups:
        for currTile in currGroup:
            tempTile = tile(currTile[0], currTile[1])
            tempGroup.append(tempTile)
            tilesToRemove.append(tempTile)
        try:
            outGroups.append(group(tempGroup))

        except GroupError:
            print('That is not a valid group')

        except SetError:
            print('That is not a valid set')

        except RunError:
            print("That is not a valid run")

        except UniqueColorError:
            print('The tiles in your set do not have unique colors')
        
        except InvalidJokerError:
            print("That is not a valid spot for a joker")
    
    return outGroups, tilesToRemove

def calculateOutGroupsValue(outGroups):
    """
    ([group]) -> int

    Calculates the value of a list of groups based on the rules of rummikub. Numbers are
    worth the same number of points as themselves and jokers are 0 points
    """
    outGroupsValue = 0
    for currGroup in outGroups:
        for currTile in currGroup.group:
            if currTile.value != 0:
                outGroupsValue += currTile.value
    
    return outGroupsValue