from tile import tile
from group import GroupError, InvalidJokerError, RunError, SetError, UniqueColorError, group
class hand():
    def __init__(self, drawPile, playerNum, customHand):
        '''
        Initialize a hand. Hand is a list that contains tiles
        '''
        self.hand = []
        self.playerNum = playerNum
        self.playedTiles = False
        self.goneOut = False
        self.hasWon = False
        if not customHand:
            self.initialDraw(drawPile)
    
    def draw(self, drawPile):
        '''
        Adds the next tile from the draw pile to hand. Increments current tile target in drawpile.
        '''
        if drawPile.currentTile >= len(drawPile.drawPile):
            print("Reached Maximum Tile, no tiles to distribute")
        else:
            self.hand.append(drawPile.drawPile[drawPile.currentTile])
    
        drawPile.currentTile += 1
    
    def initialDraw(self, drawPile):
        '''
        Draws standard hand worth of tiles into hand.
        '''
        standardHand = 14

        for i in range(standardHand):
            self.draw(drawPile)
    
    def resetHand(self, drawPile):
        """
        (self, [tile]) -> None

        resets hand to an empty hand for use with addCustomHand and resets drawPile to 
        start at the top of the pile.
        """
        self.hand = []
        drawPile.currentTile = 0

    def removeItemsFromHand(self, tilesAddedToBoard):
        """
        (self, [tiles]) -> None
        
        Given list of tiles added to the board, removes the tiles that are added to 
        the board from the hand
        """
        currHand = self.hand[:]
        TilesToRemove = []
        tempHand = []
        for currTile in tilesAddedToBoard:
            TilesToRemove.append([currTile.value, currTile.color])

        for currTile in currHand:
            tempHand.append([currTile.value, currTile.color])
        
        for currTile in TilesToRemove:
            tempHand.remove(currTile)

        currHand = []
        for currTile in tempHand:
            currHand.append(tile(currTile[0], currTile[1]))
        
        self.hand = currHand

    def addCustomHand(self, userInput):
        """
        (self, string) -> None or 0
        
        add a customHand to self.hand instead of using the intial draw method for 
        testing purposes and using the solving functions
        """
        if userInput == "":
            print('No groups submitted. Try again')
            return 0

        tempList = userInput.split(" ")
        newHand = []
        for currTile in tempList:
                tempTile = tile(int(currTile[1:]), currTile[0])
                newHand.append(tempTile)

        self.hand = newHand
        
    def displayHand(self):
        '''
        Print out tiles in hand separated by spaces in a 5 wide table
        '''
        count = 0
        if self.playerNum == -1:
            print("Solver Hand\n")
        else:
            print("\nPlayer {} Hand\n".format(self.playerNum + 1))
        for handTile in self.hand:
            if count % 5 == 0 and count > 0:
                print("\n")
            print(handTile.cstring, end=' ')
            count += 1
        print("\n", end='')
        

    def validateInput(self, userInput, goneOut, selection=[]):
        """
        (self, string, bool, [group]) -> [group] or 0

        Validates that input from a string can be converted into a set of tiles, then checks
        that the input can work as groups, then makes sure that all tiles are from selected
        groups or from the players hand
        """
        #
        if userInput == "":
            print('No groups submitted. Try again')
            return 0
        userInput = userInput.split(' | ')
        tempList = []
        for currGroup in userInput:
            tempList.append(currGroup.split(' '))

        groupsToAdd = []
        tempHand = self.hand[:]
        tempBoard = []
        for currGroup in selection:
            for currTile in currGroup.group:
                tempBoard.append(currTile)

        for i in tempList:
            tempGroup = []
            for j in i:
                tempTile = tile(int(j[1:]), j[0])

                broke = False
                for currTile in tempBoard+tempHand:
                    if currTile.value == tempTile.value and currTile.color == tempTile.color:
                        try:
                            tempBoard.remove(currTile)
                        except:
                            tempHand.remove(currTile)
                        broke = True
                        break
                

                if not broke:
                    print("Tile not in hand")
                    return 0
                
                tempGroup.append(tempTile)

            try:
                groupsToAdd.append(group(tempGroup))

            except GroupError:
                print('That is not a valid group')
                return 0

            except SetError:
                print('That is not a valid set')
                return 0

            except RunError:
                print("That is not a valid run")
                return 0

            except UniqueColorError:
                print('The tiles in your set do not have unique colors')
                return 0
            
            except InvalidJokerError:
                print("That is not a valid spot for a joker")
                return 0

        totalValue = 0
        for currGroup in groupsToAdd:
            totalValue += currGroup.getGroupValue()
        
        if goneOut:
            if len(tempHand) < len(self.hand):
                if len(tempBoard) == 0:
                    self.hand = tempHand
                    if len(tempHand) == 0:
                        self.hasWon == True
                    return groupsToAdd
                else:
                    print("Didn't include all tiles from board selection")
                    return 0
            else:
                print("Didn't add any tiles from hand")
                return 0
        elif totalValue >= 30:
            self.hand = tempHand
            return groupsToAdd
        else:
            print('Not enough points')
            return 0
    
