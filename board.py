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
        print(*['Group {}: [{}]'.format(i+1,', '.join(boardGroup)) for i, boardGroup in enumerate(self.board)], sep='\n')

    def add(self,group):
        '''
        add a group to the board
        '''
        self.board.append(group)

    def remove(self, groupIndex):
        '''
        remove a group from the board based on index
        '''
        return self.board.pop(groupIndex)

    def makeSelection(self, selectionIndices):
        '''
        take in indices, return groups from the board with those indices
        '''
        self.selection = [self.board[int(i)] for i in selectionIndices.split(' ')] 

    def displaySelection(self):
        '''
        print out selected groups from makeSelection()
        '''