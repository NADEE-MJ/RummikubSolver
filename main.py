from goingOutSolver import goingOutSolver
from hand import hand
from drawpile import drawPile
from board import board
from group import group
from tile import colors
from solver import solver as dannySolver
import os
import time

def main():
    d = drawPile()
    b = board()

    print("Welcome to RUMMIKUB\n")

    menu = """
MENU
1. Play Tiles
2. End Turn
3. Solve(GoingOutSolve or FullSolve)
Enter: """

    colorKey = f"Color Key:\n{colors.colorsDict['R']}R = Red \n\
{colors.colorsDict['B']}B = Blue \n\
{colors.colorsDict['Y']}Y = Yellow \n\
{colors.colorsDict['K']}K = Black \n\
{colors.colorsDict['E']}J = Joker\n"

    valueKey = """Value Key:
1 - 13 = same value as number
Jokers or J0 = has no value\n"""

    print(colorKey)
    print(valueKey)

    while True:
        gameOver = False
        numPlayers = input("How many people are playing? (2, 3, or 4) ")
        #numPlayers = 'solver' #for testing goingOutSolver

        if numPlayers in ['2', '3', '4']:
            players = [hand(d, i, False) for i in range(int(numPlayers))]

        elif numPlayers == 'solver':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("CHEAT CODE ENTERED\nRunning solver....")
            #time.sleep(2)
            solver = hand(drawPile(), -1, True)

            boardInputed = False
            for i in range(106):
                solver.draw(d)
            while not gameOver:
                if not boardInputed:
                    solverBoard = input("Enter your board in the following format: (R1 R2 R3 | R4 B4 Y4) ")
                    if not solverBoard == '':
                        boardTiles = solver.validateInput(solverBoard, True)
                        if boardTiles == 0:
                            continue
                        else:
                            b.addGroups(boardTiles)
                            boardInputed = True
                
                b.displayBoard()
                
                solver.resetHand(d)
                solverHand = input("Enter your hand in the following format: (R1 R2 R3) ")
                handTiles = solver.addCustomHand(solverHand)
                if handTiles == 0:
                    continue
                else:
                    solver.displayHand()
                    while True:
                        solverPrefence = input("Which solver do you want to use? (GoingOutSolver == 'g' and Solver == 's')")
                        if solverPrefence in  ['g', 'G']:
                            solverGoingOutGroups, tilesToRemove = goingOutSolver(solver.hand)
                            if not solverGoingOutGroups == None:
                                b.addGroups(solverGoingOutGroups)
                                solver.removeItemsFromHand(tilesToRemove)
                                b.displayBoard()
                                solver.displayHand()
                            gameOver = True
                            break
                        elif solverPrefence in ['s', 'S']:
                            groupsToAdd, newHand = dannySolver(solver.hand, b.selectAllGroups())
                            if groupsToAdd != None:
                                b.addGroups(groupsToAdd)
                                solver.hand = newHand
                                b.displayBoard()
                                solver.displayHand()
                            else:
                                b.reinsertSelection()
                            gameOver = True
                            break
                        else:
                            print("That is not valid input!")
                            continue

        else:
            print('\n"{}" is not valid input! Please input 2, 3, or 4!'.format(numPlayers))
            continue

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
                                continue
                            else:
                                b.addGroups(addingTiles)
                                if player.hasWon:
                                    b.displayBoard()
                                    print("Player {} has won!".format(player.playerNum))
                                    gameOver = True
                                    break
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
                        if not player.goneOut:
                            #goingOutSolver
                            os.system('cls' if os.name == 'nt' else 'clear')
                            b.displayBoard()
                            player.displayHand()
                            playerGoingOutGroups, tilesToRemove = goingOutSolver(player.hand)
                            if not playerGoingOutGroups == None:
                                b.addGroups(playerGoingOutGroups)
                                player.removeItemsFromHand(tilesToRemove)
                                player.goneOut = True
                                os.system('cls' if os.name == 'nt' else 'clear')
                            continue

                        else:
                            #solver
                            os.system('cls' if os.name == 'nt' else 'clear')
                            b.displayBoard()
                            player.displayHand()
                            groupsToAdd, newHand = dannySolver(player.hand, b.selectAllGroups())
                            if groupsToAdd != None:
                                b.addGroups(groupsToAdd)
                                player.hand = newHand
                                b.displayBoard()
                                player.displayHand()
                            else:
                                b.reinsertSelection()
                            os.system('cls' if os.name == 'nt' else 'clear')
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