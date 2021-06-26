from tile import tile
import random

class drawPile():
    def __init__(self):
        """
        () -> drawPile

        Initializer for the drawPile class. Creates a drawPile list, then adds all tiles to the list, then shuffles the drawPile list.
        """

        self.drawPile = []
        self.createPile()
        self.shuffle()

    def createPile(self):
        """
        () -> ()

        Initializes the drawPile list for the object. Adds 106 tile objects to the drawPile list.
        Adds 2 joker tiles and 26 tiles of each color: R(Red), B(Blue), Y(Yellow), K(Black)
        Includes tiles ranging from 1 to 13. (Two of each number per color)
        """
        highestValue = 13
        numberOfJokers = 2
        numberOfEachTile = 2
        self.maxTile = 0
        for i in range(1, highestValue + 1):
            for _ in range(0, numberOfEachTile):
                self.drawPile.append(tile(i, 'R'))
                self.drawPile.append(tile(i, 'B'))
                self.drawPile.append(tile(i, 'Y'))
                self.drawPile.append(tile(i, 'K'))
                self.maxTile += 4
        for i in range(0, numberOfJokers):
            self.drawPile.append(tile(0, 'J'))
            self.maxTile += 1

    def shuffle(self):
        """
        () -> ()

        Shuffles the drawPile and sets the currentTile to the index of the first tile in the
        list, which starts at zero. As tiles are drawn currentTile is incremented. 
        """
        
        self.currentTile = 0
        random.shuffle(self.drawPile)
