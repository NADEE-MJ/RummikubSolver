# RummikubSolver
Text based Rummikub game and solver created for Hackathon-x Vol 2 in June 2021

## How the game works
First the game asks user to enter how many people are playing. Each player is dealt 14 tiles. Players have the option to place tiles(1), end their turn(2), or use the solvers(3) (forfeit the win). If the player selects option (1) then they are able to place tiles onto the board. If the player has not already placed tiles adding up to a score of 30 onto the board they must first do so in order to play more tiles onto existing groups in the board. If the player selects option (2) it will skip to the next players turn. If the player has not played any tiles that turn ending their turn will auto draw a tile. If the player selects option (3) then they can use either of the solvers to instantly solve the border based off that solvers algorithm. In order to win the player must get rid of all their tiles, only using option (1).

## How the solver works
The solver first generates an exhaustive list of every possible unique group. It then compares each group to the tiles present in the player's hand and on the board to determine which groups can possibly be played. It runs through each group and all following groups to determine the best possible collection of groups to maximize the number of tiles played.

## How the goingOutSolver works
Going out is the first step in adding tiles to the board in rummikub. In order to play any tiles to the board you must first place down enough unique groups from your hand to equal 30 points in total from your hand. GoingOutSolver optimizes for finding the easiest way to play 30 points onto the board. It first checks if the player's hand has any sets in their hand, then checks for runs, then for sets and runs with jokers. This does not account for all edge cases, although it may be able to with some tweaking. If time permits, will try to write a goingOutSolver using the same algorithm as the solver function.

## Inputting custom board and hand
When the game asks for the number of users, the cheatcode "solver" will allow you to input a custom board and hand. This will allow you to use either algorithm to see if the game is in a solvable state or if you can go out based on the chosen algorithm.

## What we need to add
1. GUI
2. Fix algorithms to include all edge cases
3. Add ILP as a third solving method
4. Make codestyle more consistent