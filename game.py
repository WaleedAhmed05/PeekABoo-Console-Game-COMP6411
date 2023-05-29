"""
Author: WaleedAhmed05
Date: May 25, 2023
Description: This file contains code for the user interface (i.e., the menu, the various user prompts,
error messages, and the display of the final score)
"""
from grid import Grid
from grid import Score
import sys
import time
import os

class Main():
    size=None
    gridX=None
    score=None
    configScreen=None
    cheatDetector=True #check if user chose option 2 for all cells.
    unCoverCounter=0
    boardMessage=""

    def __init__(self,size):
        self.size = size
        self.gridX = Grid(self.size)
        self.score= Score(self.size)

        if os.name == 'nt':  # Windows
            self.configScreen="cls"
        elif os.name == 'posix':  # Linux/Unix/Mac
            self.configScreen="clear"
        else:
            self.configScreen="clear" #default


    def printScreen(self,programFlag=True):
        os.system(self.configScreen)
        print("---------------------\n"
              "|    PEEK-A-BOO     |\n"
              "---------------------\n")

        if(programFlag):
            self.gridX.randArray()

        self.gridX.blankGrid()
        print("\n")
        print(self.boardMessage)
        print("1. Let me select two elements\n"
              "2. Uncover one element for me\n"
              "3. I give up - reveal the grid\n"
              "4. New game\n"
              "5. Exit\n")        #Menu.

    def setBoardMessage(self,message):
        if(message==""):
            self.boardMessage = str(message)
        else:
            self.boardMessage = str(message) + "\n"



    def menu(self):
        userInput=0
        while userInput!='5':
            userInput=input("Select: ")


            if (userInput=='1'): #option 1
                element1="x9" #coordinate #1
                firstCharflag=True
                secondCharFlag=True

                while (firstCharflag):  # Validating cell coordinates.

                    element1 = input("Enter cell coordinates (e.g., a0): ").lower()
                    if(len(element1)!=2):
                        print("input error: cell coordinate should be 2 characters in length! Please try again.")

                    elif((not element1[0].isalpha()) or (not element1[1].isdigit())):
                        print("input error: cell coordinate is invalid! Please try again.")

                    elif((ord(element1[0]) < 97) or (ord(element1[0]) > (96 + self.size)) or
                            (int(element1[1]) < 0) or (int(element1[1]) > self.size - 1)):
                        print("input error: row entry is out of range for this grid. Please try again.")

                    else:
                        firstCharflag=False

                element2="x9" #coordinate #2
                while (secondCharFlag):  # Validating cell coordinates for element 2.

                    element2 = input("Enter cell coordinates (e.g., b0): ").lower()
                    if (len(element2) != 2):
                        print("input error: cell coordinate should be 2 characters in length! Please try again.")

                    elif ((not element2[0].isalpha()) or (not element2[1].isdigit())):
                        print("input error: cell coordinate is invalid! Please try again.")

                    elif (element1 == element2):
                        print("input error: duplicate entry! Please try again.")

                    elif ((ord(element2[0]) < 97) or (ord(element2[0]) > (96 + self.size)) or
                            (int(element2[1]) < 0) or (int(element2[1]) > self.size - 1)):
                        print("input error: row entry is out of range for this grid. Please try again.")
                    else:
                        secondCharFlag=False #correct input added / break from loop


                index1=((self.size*int(element1[1])) + (ord(element1[0])-97))
                index2=((self.size*int(element2[1])) + (ord(element2[0])-97))
                self.score.countGuess(1) #count 1 guess


                if(not self.gridX.checkCell(index1,index2)): #if elements are not same give a glimpse for 2 seconds.

                    isIndex1AlreadyVisible=self.gridX.checkVisibility(index1) #if chosen index already visible.
                    isIndex2AlreadyVisible=self.gridX.checkVisibility(index2)

                    self.gridX.updateCell(index1,index2)
                    self.printScreen(False)
                    time.sleep(2)
                    self.gridX.switchBacktoHide(index1,index2)
                    if isIndex1AlreadyVisible: #if index was visible before, then let it remain visible.
                            self.gridX.unCoverCell(index1)
                    if isIndex2AlreadyVisible:
                            self.gridX.unCoverCell(index2)

                    self.printScreen(False)

                else: #if elements have same value, make them visible to board
                    self.gridX.updateCell(index1, index2)
                    self.cheatDetector=False  #player successfully selected right pairs.
                    self.printScreen(False)


                if (all(self.gridX.getrandFlag())):
                    self.setBoardMessage("Game Ended! Your Score! " + "{:.2f}".format(self.score.getScore()))
                    self.printScreen(False)
                    userInput = '5'



            elif(userInput=='2'):
                option2Inputflag=True

                while (option2Inputflag):  # Validating cell coordinates for element 2.


                    index1 = input("Enter cell coordinates (e.g., a0): ").lower()


                    if (len(index1) != 2):
                        print("input error: cell coordinate should be 2 characters in length! Please try again.")

                    elif ((not index1[0].isalpha()) or (not index1[1].isdigit())):
                        print("input error: cell coordinate is invalid! Please try again.")


                    elif ((ord(index1[0]) < 97) or (ord(index1[0]) > (96 + self.size)) or
                       (int(index1[1]) < 0) or (int(index1[1]) > self.size - 1)):
                        print("input error: row entry is out of range for this grid. Please try again.")


                    else:
                        intIndex1 = ((self.size * int(index1[1])) + (ord(index1[0]) - 97))
                        self.unCoverCounter+=1
                        option2Inputflag=False
                        self.score.countGuess(2)
                        self.gridX.unCoverCell(intIndex1)
                        self.gridX.updateUnCoverElements(intIndex1)
                        self.printScreen(False)



                if (self.unCoverCounter >= (self.size ** 2) and all(self.gridX.getunCoverElements())):
                    self.setBoardMessage("You cheated - Loser! Your score is 0!")
                    self.printScreen()
                    userInput='5'#end game.

                elif(all(self.gridX.getrandFlag())):
                    self.setBoardMessage("Game Ended! Your Score! " + "{:.2f}".format(self.score.getScore()))
                    self.printScreen()
                    userInput='5'





            elif(userInput=='3'):
                self.setBoardMessage("")
                self.gridX.revealGrid()
                self.printScreen(False)
                userInput='5' #end game.

            elif(userInput=='4'):
                self.score.resetScore()
                self.gridX.resetGame()
                self.gridX.randArray()
                self.setBoardMessage("")
                self.printScreen()



if __name__ == '__main__':
    # Code to be executed when the script is run directly
    sizeX = sys.argv[1]
    # Restricting the grid size to be either 2,4 or 6 to follow assignment requirement.
    if (sizeX == '2' or sizeX == '4' or sizeX == '6'):
        myinstance = Main(int(sizeX))
        myinstance.printScreen()
        myinstance.menu()
    else:
        print("Invalid Grid size!")



