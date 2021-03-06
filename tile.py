class colors:
    colorsDict = {'R': '\033[91m',\
                    'B': '\033[94m',\
                    'Y': '\033[93m',\
                    'K': '\033[92m',\
                    'E': '\033[0m',\
                    'J': '\033[0m'}

class tile():
    def __init__(self, value, color):
        """
        (self, int, char) -> tile 

        Initializer for tile class.
        """
        self.value = value
        self.color = color
        self.string = self.stringFormat()
        self.cstring = self.coloredStringFormat()
        
    def stringFormat(self):
        """
        (self) -> string
        
        returns the name of the tile formatted as a string
        """
        return "{}{}".format(self.color, self.value)

    def coloredStringFormat(self):
        """
        (self) -> string
        
        returns the name of the tile formatted as a string with the proper color
        """
        return f"{colors.colorsDict[self.color]}{self.string}{colors.colorsDict['E']}"