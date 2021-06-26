class hand():
    def __init__(self, drawPile, player):
        '''
        Initialize a hand. Hand is a list that contains tiles
        '''
        self.hand = []
        self.player = player
        self.goneOut = False
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
        printable = []
        for handTile in self.hand:
            printable.append('{}{}'.format(handTile.color,handTile.value))
        print("\nPlayer {}\n".format(self.player + 1))
        print(*printable, sep='  ')