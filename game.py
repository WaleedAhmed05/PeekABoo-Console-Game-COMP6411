from grid import Grid
import sys
import time
import os

class Main():
    size=None
    gridX=None
    score=None
    boardMessage=""

    def __init__(self,size):
        self.size = size
        self.gridX = Grid(self.size)
        self.score= Score(self.size)


    def printScreen(self,programFlag=True):
        os.system("cls")
        #TODO change this command to linux command.
        print("---------------------\n"
              "|    PEEK-A-BOO     |\n"
              "---------------------\n")
        #Grid.randArray(4)
        if(programFlag):
            self.gridX.randArray()

        self.gridX.blankGrid()
        print("\n")
        print(self.boardMessage)
        print("\n")
        print("1. Let me select two elements\n"
              "2. Uncover one element for me\n"
              "3. I give up - reveal the grid\n"
              "4. New game\n"
              "5. Exit\n")        #Menu.

    def setBoardMessage(self,message):
        self.boardMessage=message

    def menu(self):
        userInput=0
        while userInput!='5':
            userInput=input("Select: ")

            if (userInput=='1'):
                element1="x9"
                while ((ord(element1[0]) < 97) or (ord(element1[0]) > (96 + self.size)) or
                       (int(element1[1]) < 0) or (int(element1[1]) > self.size - 1)):  # Validating cell coordinates.

                    element1 = input("Enter cell coordinates (e.g., a0): ").lower()
                    if ((ord(element1[0]) < 97) or (ord(element1[0]) > (96 + self.size)) or
                            (int(element1[1]) < 0) or (int(element1[1]) > self.size - 1)):
                        print("input error: row entry is out of range for this grid. Please try again.")

                element2="x9"
                while ((ord(element2[0]) < 97) or (ord(element2[0]) > (96 + self.size)) or
                       (int(element2[1]) < 0) or (int(element2[1]) > self.size - 1) or
                       element1 == element2):  # Validating cell coordinates for element 2.

                    element2 = input("Enter cell coordinates (e.g., b0): ").lower()
                    if ((ord(element2[0]) < 97) or (ord(element2[0]) > (96 + self.size)) or
                            (int(element2[1]) < 0) or (int(element2[1]) > self.size - 1) or
                            element1 == element2):
                        print("input error: row entry is out of range for this grid. Please try again.")


                index1=((self.size*int(element1[1])) + (ord(element1[0])-97))
                index2=((self.size*int(element2[1])) + (ord(element2[0])-97))


                if(not self.gridX.checkCell(index1,index2)):
                    self.gridX.updateCell(index1,index2)
                    self.printScreen(False)
                    time.sleep(2)
                    self.gridX.switchBacktoHide(index1,index2)
                    self.printScreen(False)


                #gridX.updateCell(index1,index2)
                # do this
            elif(userInput=='2'):
                index1 = "x9"
                visibilityflag=True

                while ((ord(index1[0]) < 97) or (ord(index1[0]) > (96 + self.size)) or
                       (int(index1[1]) < 0) or (int(index1[1]) > self.size - 1) or
                visibilityflag):  # Validating cell coordinates for element 2.

                    index1 = input("Enter cell coordinates (e.g., a0): ").lower()
                    intIndex1 = ((self.size * int(index1[1])) + (ord(index1[0]) - 97))


                    if ((ord(index1[0]) < 97) or (ord(index1[0]) > (96 + self.size)) or
                       (int(index1[1]) < 0) or (int(index1[1]) > self.size - 1)):
                        print("input error: row entry is out of range for this grid. Please try again.")

                    elif (self.gridX.checkVisibility(intIndex1)):
                        print("input error: element is already visible! ")

                    else:
                        visibilityflag=False
                        self.score.countGuess(2)
                        self.gridX.unCoverCell(intIndex1)
                        self.printScreen(False)

                if (False in self.gridX.getrandFlag()):
                    self.setBoardMessage("hello")



            # do this
            elif(userInput=='3'):
                self.gridX.revealGrid()
                self.printScreen(False)
                userInput='5'
                # do this
            elif(userInput=='4'):
                #TODO score reset.
                self.gridX.resetGame()
                self.gridX.randArray()
                self.printScreen()
            self.printScreen()

class Score:

    score=None
    guessAttempts=0
    minimum_possible_guesses=None

    def __init__(self,sizeXx):
        self.minimum_possible_guesses=sizeXx*2

    def countGuess(self,guess):
        self.guessAttempts+=guess
    def getScore(self,score):
        #Score = (minimum_possible_guesses / actual_guesses) * 100
        return self.score
    def setScore(self,score):
        self.score=score
    def updateScore(self,guess_attempt):
        print("")



sizeX=sys.argv[1]
#Restricting the grid size to be either 2,4 or 6 to follow assignment requirement.
if(sizeX=='2' or sizeX=='4' or sizeX=='6'):
    myinstance = Main(int(sizeX))
    myinstance.printScreen()
    myinstance.menu()
else:
    print("Invalid Grid size!")


