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
        self.hand = []
        drawPile.currentTile = 0

    def addCustomHand(self, userInput):
        if userInput == "":
            print('No groups submitted. Try again')
            return 0

        tempList = userInput.split(" ")
        newHand = []
        for el in tempList:
                tempTile = tile(int(el[1:]), el[0])
                newHand.append(tempTile)

        self.hand = newHand
        

    # def displayHand(self):
    #     # print out hand using list comprehension (better)
    #     '''
    #     Print out tiles in hand separated by tabs
    #     '''
    #     print(*['{}{}'.format(handTile.color,handTile.value) for handTile in self.hand], sep='\t')
    
    def displayHand(self):
        # print out hand not using list comprehension (worse)
        '''
        Print out tiles in hand separated by tabs
        '''
        count = 0
        if self.playerNum == -1:
            print("Solver Hand\n")
        else:
            print("\nPlayer {} Hand\n".format(self.playerNum + 1))
        for handTile in self.hand:
            if count % 5 == 0 and count > 0:
                print("\n")
            print(handTile.string, end=' ')
            count += 1
        print("\n", end='')
        

    def validateInput(self, userInput, goneOut, selection=[]):
        if userInput == "":
            print('No groups submitted. Try again')
            return 0
        userInput = userInput.split(' | ')
        tempList = []
        for groupo in userInput:
            tempList.append(groupo.split(' '))

        groupsToAdd = []
        tempHand = self.hand[:]
        tempBoard = []
        for groupo in selection[:]:
            for el in groupo.group:
                tempBoard.append(el)

        for i in tempList:
            tempGroup = []
            for j in i:
                tempTile = tile(int(j[1:]), j[0])

                broke = False
                for el in tempBoard+tempHand:
                    if el.value == tempTile.value and el.color == tempTile.color:
                        try:
                            tempBoard.remove(el)
                        except:
                            tempHand.remove(el)
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
        for groupo in groupsToAdd:
            totalValue += groupo.getGroupValue()
        
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
    