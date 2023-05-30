# PeekABoo
Peek A Boo, a console based grid game built with Python 3.
Assignment-01 COMP6411 - Comparative Study of Programming Languages @ Concordia University.

### Short Summary
The game will display a square grid, with the columns labeled with letters, and the rows with numbers. Player job is to find the hidden pairs in as few
guesses as possible. <br>
![Main menu](https://github.com/WaleedAhmed05/PeekABoo/blob/GameInterface/Main_menu.png?raw=true)

## Commands
Run this command to start game, choose grid size as either 2,4 or 6.
```
python game.py 4
```
Option 1: Player has to choose two coordinates to make a pair of same numbers.
```
a0 b1
```
![Option 1](https://github.com/WaleedAhmed05/PeekABoo/GameInterface/blob/option_1.png?raw=true)

Option 2: Player can choose any co-ordinate to uncover cell.
```
a1
```
![Option 2](https://github.com/WaleedAhmed05/PeekABoo/GameInterface/blob/option_2.png?raw=true)

Lastly, player final score is based on their total guesses, such that your guesses will be divided by minimum guess required to calculate final score.
![Final Score](https://github.com/WaleedAhmed05/PeekABoo/GameInterface/blob/Final_score.png?raw=true) 

## Game Parameters & Rules.
Initially grid size is restricted to either 2x2, 4x4 or 6x6 dimension, but it can be changed to any even size.
```
    if (sizeX == '2' or sizeX == '4' or sizeX == '6'): #change this condition to (sizeX%2==0)
        myinstance = Main(int(sizeX))
        ...
        ...
```









