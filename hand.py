from tile import tile

class hand():
    def __init__(self):
        self.hand = []
    
    def draw(self, drawPile):
        self.hand.append(drawPile.drawPile[drawPile.currentTile])
        drawPile.currentTile += 1

    def initialDraw(self, drawPile):
        standardHand = 14

        for i in range(standardHand):
            self.draw(drawPile)
    
    # def displayHand(self):
    #     # print out hand using list comprehension (better)
    #     print(*[handTile.color + str(handTile.value) for handTile in self.hand], sep='\t')
    
    def displayHand(self):
        # print out hand not using list comprehension (worse)
        printable = []
        for handTile in self.hand:
            printable.append(handTile.color + str(handTile.value))
        print(*printable, sep='\t')