class board():
    def __init__(self):
        self.board = []

    def displayBoard(self):
        '''
        print out the contents of the group

        Group 1: [B4, B5, B6]
        Group 2: [R10, B10, K10]
        ...
        '''
        print('BOARD')
        print(*['Group {}: [{}]'.format(i+1,', '.join(boardGroup)) for i, boardGroup in enumerate(self.board)], sep='\n')

    def addGroups(self,groups):
        '''
        add a group to the board
        '''
        self.board.extend(groups)


    def removeGroups(self, groups):
        '''
        remove a group from the board based on index
        '''
        for group in groups:
            self.board.remove(group)

    def makeSelection(self, selectionIndices):
        '''
        take in indices, return groups from the board with those indices
        '''
        self.selection = [self.board[int(i)] for i in selectionIndices.split(' ')]
        self.removeGroups(self.selection)

    def displaySelection(self):
        '''
        print out selected groups from makeSelection()
        '''
        print('SELECTED GROUPS')
        print(*['[{}]'.format(', '.join(selectedGroup)) for selectedGroup in self.selection], sep='\n')
    
    def reinsertSelection(self):
        '''
        if the group(s) submitted by the player are invalid, return the selection to the board
        empty the selection
        '''
        self.board.extend(self.selection)
        self.selection = []