class GroupError(Exception):
    pass

class SetError(Exception):
    pass

class RunError(Exception):
    pass

class UniqueColorError(Exception):
    pass

class InvalidJokerError(Exception):
    pass

class group():

    def __init__(self, group):
        """
        ([tile]) -> group

        Initializer for the group class, will create a group list from input list of tiles
        then check if that group is a valid set or run
        """
        self.group = group
        self.groupValidity()

    def groupValidity(self):
        """
        () -> Exception?

        Checks whether group is valid based on the constraints of a either a set or run. If
        the group conforms to a set or run then no exception is raised, otherwise a specific
        exception is raised.
        """

        #check at least 3 tiles in group and less than 13 tiles in group
        if len(self.group) >= 3 + len(self.group) <= 13:
            #set check (same number)
            setCheck = True

            #get starting number
            for tile in self.group:
                if tile.value != 0:
                    tempNum = tile.value
                    break

            #check all numbers are the same or a joker
            for tile in self.group:
                if tile.value == tempNum or tile.value == 0:
                    continue
                else:
                    setCheck = False
                    break

            #set max length check
            if setCheck:
                if len(self.group) <= 4:
                    #unique colors check
                    usedColors = []
                    for tile in self.group:
                        if tile.color in usedColors:
                            raise UniqueColorError
                        else:
                            usedColors.append(tile.color)
                else:
                    raise SetError

            #run check (same color)
            #get starting color
            for tile in self.group:
                if tile.color != 'J':
                    tempColor = tile.color
                    break

            #check all colors are the same or a joker
            for tile in self.group:
                if tile.color == tempColor or tile.color == 'J':
                    continue
                else:
                    raise GroupError

            #finds first number in a run
            jokerCount = 0
            for tile in self.group:
                if tile.value != 0:
                    tempNum = tile.value - jokerCount - 1
                    break
                else:
                    jokerCount += 1

            #checks each tile in a run is sequential
            numbersInGroup = []
            for tile in self.group:
                if tile.value == tempNum + 1 or tile.value == 0:
                    if tile.value > 0:
                        tempNum = tile.value
                        numbersInGroup.append(tempNum)
                    else:
                        tempNum += 1
                        numbersInGroup.append(0)
                else:
                    raise RunError
            
            #Tenshis way
            for i in range(1, len(self.group)):
                if self.group[i] > self.group[i - 1] or self.group[i] == 0:
                    if self.group[i] != 0:
                        numbersInGroup.append(self.group[i])
                    else:
                        numbersInGroup.append(0)

            #count the number of jokers in the run
            jokerCount = 0
            for tile in self.group:
                if tile.value == 0:
                    jokerCount += 1

            #check if there is a joker at the left or right of a run
            if jokerCount == 1:
                if 1 in numbersInGroup and self.group[0] != 1:
                    raise InvalidJokerError
                if 13 in numbersInGroup and self.group[-1] != 13:
                    raise InvalidJokerError

            elif jokerCount == 2:
                if 1 in numbersInGroup and self.group[0] != 1:
                    raise InvalidJokerError
                if 2 in numbersInGroup and self.group[2] == 2:
                    raise InvalidJokerError
                if 12 in numbersInGroup and self.group[-3] == 12:
                    raise InvalidJokerError
                if 13 in numbersInGroup and self.group[-1] != 13:
                    raise InvalidJokerError

        else:
            raise GroupError