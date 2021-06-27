class board():
    def __init__(self):
        '''
        Initialize board class. Make an empty list for the board to hold groups
        '''
        self.board = []

    def displayBoard(self):
        '''
        print out the contents of the group

        Group 1: [B4, B5, B6]
        Group 2: [R10, B10, K10]
        ...
        '''
        print('BOARD')
        if len(self.board) == 0:
            print('The board is empty')
        else:
            for i, boardGroup in enumerate(self.board):
                print('Group {}: '.format(i), end=' ')
                for el in boardGroup.group:
                    print(el.cstring, end=' ')
                print('\n', end='')
            # print(*['Group {}: [{}]'.format(i,', '.join(boardGroup.group)) for i, boardGroup in enumerate(self.board)], sep='\n')

    def addGroups(self,groups):
        '''
        add a group to the board
        '''
        self.board.extend(groups)
        self.selection = []

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
        print('SELECTED GROUPS TILES')
        for selectedGroup in self.selection:
            for el in selectedGroup.group:
                print(el.cstring, end=' ')
        print('\n',end='')

        #print(*['[{}]'.format(', '.join(selectedGroup)) for selectedGroup in self.selection], sep='\n')

    def selectAllGroups(self):
        """
        Select all groups on board
        """
        self.selection = self.board[:]
        self.removeGroups(self.selection)

        return self.selection
    
    def reinsertSelection(self):
        '''
        if the group(s) submitted by the player are invalid, return the selection to the board
        empty the selection
        '''
        self.board.extend(self.selection)
        self.selection = []