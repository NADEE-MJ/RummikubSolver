class tile():
    def __init__(self, value, color):
        """
        (self, int, char) -> tile 

        Initializer for tile class.
        """
        self.value = value
        self.color = color
        self.string = self.stringFormat()
        
    def stringFormat(self):
        return "{}{}".format(self.color, self.value)