from tile import tile

class hand():
    def __init__(self):
        self.hand = []
    
    def draw(self, drawpile):
        self.hand.append('something something tile somehting')

    def initialDraw(self, drawpile):
        standardHand = 14

        for i in range(standardHand):
            self.draw(drawpile)
    
    def displayHand(self):
        print(*[handTile.color + str(handTile.value) for handTile in self.hand], sep='\t')
            