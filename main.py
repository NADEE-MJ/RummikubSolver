from hand import hand
from drawpile import drawPile
from board import board
from group import group
import os

def main():
    d = drawPile()
    b = board()

    print("Welcome to RUMMIKUB\n")

    menu = """
MENU
1. Play Tiles
2. End Turn
3. Solve
Enter: """

    colorKey = """Color Key:
R = Red
B = Blue
Y = Yellow
K = Black
J = Joker\n"""

    valueKey = """Value Key:
1 - 13 = same value as number
Jokers or J0 = has no value\n"""

    print(colorKey)
    print(valueKey)

    while True:
        gameOver = False
        numPlayers = input("How many people are playing? (2, 3, or 4) ")

        if numPlayers in ['2', '3', '4']:
            players = [hand(d, i) for i in range(int(numPlayers))]

        # elif numPlayers == 'solver':
        #     print("Nice try hacker!")
        #     b.board = input("Enter your board in the following format: ([[..,..]]) Ex: [[R1, R2, R3],  [R1, B1, Y1, G1]] ")
            
        #     h1 = hand()
        #     h1.hand = input("Enter your hand in the following format: ([..,..]) Ex: [R1, B1, Y1, G1] ")
        #     break

        else:
            print('\n"{}" is not valid input! Please input 2, 3, or 4!'.format(numPlayers))
            continue

        os.system('cls' if os.name == 'nt' else 'clear')

        while not gameOver:
            for player in players:
                player.playedTiles = False
                while True:
                    b.displayBoard()
                    player.displayHand()
                    userChoice = input(menu)
                    if userChoice == '1':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        if player.goneOut == True:
                            #add to board
                            os.system('cls' if os.name == 'nt' else 'clear')
                            b.displayBoard()
                            player.displayHand()
                            userInput = input('Enter the group numbers you want to use: ')
                            os.system('cls' if os.name == 'nt' else 'clear')
                            if not userInput == '':
                                b.makeSelection(userInput)
                                player.displayHand()
                                userInput = input("Enter sets and runs from your hand and groups in the following format: (R1 R2 R3 | R4 B4 Y4) ")
                                addingTiles = player.validateInput(userInput, player.goneOut, b.selection)
                            else:
                                player.displayHand()
                                userInput = input("Enter sets and runs from your hand in the following format: (R1 R2 R3 | R4 B4 Y4) ")
                                addingTiles = player.validateInput(userInput, player.goneOut)

                            if addingTiles == 0:
                                b.reinsertSelection()
                                if player.hasWon:
                                    print("Player {} has won!".format(player.playerNum))
                                    gameOver = True
                                    break
                                continue
                            else:
                                b.addGroups(addingTiles)
                                player.playedTiles = True
                        else:
                            #go out
                            player.displayHand()
                            print("In order to start playing pieces on the board you need to go out, 30 points are required to do so.")
                            userInput = input("Enter sets and runs from your hand in the following format: (R1 R2 R3 | R4 B4 Y4) ")
                            goingOut = player.validateInput(userInput, player.goneOut)
                            if goingOut == 0:
                                continue
                            else:
                                b.addGroups(goingOut)
                                player.playedTiles = True
                                player.goneOut = True
                    elif userChoice == '2':
                        #end turn / draw
                        os.system('cls' if os.name == 'nt' else 'clear')
                        if not player.playedTiles:
                            player.draw(d)
                        break
                    elif userChoice == '3':
                        #solver
                        os.system('cls' if os.name == 'nt' else 'clear')
                        pass
                    else:
                        print('"{}" is not an option!\n'.format(userChoice))

                if gameOver:
                    break    
            
        playAgain = input("Would you like to play again? (y or n) ")
        if playAgain in ['y', 'Y']:
            #reset vars and continue
            d = drawPile()
            b = board()
            players = []

        elif playAgain in ['n', 'N']:       
            break
        
        else:
            print("That is not valid input try again!")


if __name__ == "__main__":
    main()