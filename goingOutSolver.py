from tile import tile
from group import GroupError, InvalidJokerError, RunError, SetError, UniqueColorError, group

def takeSecond(elem):
    return elem[1]

def goingOutSolver(solverHand):
    outGroups = []
    outGroupsValue = 0
    currHand = []
    jokerCount = 0
    for currTile in solverHand:
        currHand.append([currTile.value, currTile.color])
        if currTile.value == 0:
            jokerCount += 1
    
    #orders currHand by value descending
    currHand.sort(reverse=True)

    #check for any sets starting from end of currHand if you have two tiles over value 10
    #and a joker then the solver will add the joker to that group
    #possible to go out if you have J 9 9 and then another set or run
    temp = 0
    tempGroup = []
    tempOutGroups = []
    addedColors = []
    for currTile in currHand:
        if currTile[0] == temp and currTile[1] not in addedColors and len(tempGroup) < 5:
            tempGroup.append(currTile)
            addedColors.append(currTile[1])
            if len(tempGroup) == 4:
                tempOutGroups.append(tempGroup)
                for tileToRemove in tempGroup:
                    currHand.remove(tileToRemove)
                temp = 0
                tempGroup = []
                addedColors = []
        elif len(tempGroup) == 2 and (currTile[0] != temp and temp >= 10) and jokerCount >= 1:
            temp = currTile[0]
            tempGroup = []
            addedColors = []
            tempGroup.append([O, 'J'])
            jokerCount -= 1
        else:
            if len(tempGroup) >= 3:
                tempOutGroups.append(tempGroup)
                for tileToRemove in tempGroup:
                    currHand.remove(tileToRemove)
            temp = currTile[0]
            tempGroup = []
            addedColors = []
            tempGroup.append(currTile)
            addedColors.append(currTile[1])

    #checks for runs
    temp = 0
    tempGroup = []
    currColor = ''
    #orders currhand by value descending and then by color not accouting for jokers
    currHand.sort(reverse=True)
    currHand.sort(key=takeSecond)
    for currTile in currHand:
        if currTile[0] < temp and currTile[1] == currColor:
            tempGroup.append(currTile)
            temp = currTile[0]
        elif currTile[0] == temp and currTile[1] == currColor:
            continue
        else:
            if len(tempGroup) >= 3:
                tempOutGroups.append(tempGroup)
                for tileToRemove in tempGroup:
                    currHand.remove(tileToRemove)
            tempGroup = []
            temp = currTile[0]
            currColor = currTile[1]

    #converts list of list of lists to list of groups
    tempGroup = []
    tilesToRemove = []
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


    #calculates outGroups value
    for currGroup in outGroups:
        for currTile in currGroup.group:
            if currTile.value != 0:
                outGroupsValue += currTile.value

    #check if outGroups is worth 30 points
    if outGroupsValue >= 30:
        return outGroups, tilesToRemove
    else:
        print("Not able to go out.")
        return None, None