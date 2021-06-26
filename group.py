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
            
            numbersInGroup = []
            consJoker = 0
            currNum = 0

            if self.group[0].value == 0:
                consJoker += 1
            else:
                currNum = self.group[0].value

            for i in range(1, len(self.group)):
                if self.group[i].value == 0:
                    consJoker += 1
                    if curr_num + consJoker > 13:
                        raise InvalidJokerError
                else:
                    if consJoker > 0 and self.group[i].value - consJoker < 1:
                        raise InvalidJokerError
                    if currNum == 0:
                        currNum = self.group[i].value
                    else:
                        if self.group[i].value - consJoker - 1 != self.group[i - 1 - consJoker].value:
                            raise RunError
                        currNum = self.group[i].value

                    cons_joker = 0

