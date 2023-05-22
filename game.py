import time

from grid import Grid
import os

class Main:
    global size
    size=4
    global gridX
    gridX = Grid(size)

    def printScreen(self,programFlag=True):
        os.system("cls")
        print("---------------------\n"
              "|    PEEK-A-BOO     |\n"
              "---------------------\n")
        #Grid.randArray(4)
        if(programFlag):
            gridX.randArray()

        gridX.blankGrid()
        print("")
        #print("Here's grid X\n") #this will print grid.
        print("1. Let me select two elements\n"
              "2. Uncover one element for me\n"
              "3. I give up - reveal the grid\n"
              "4. New game\n"
              "5. Exit\n")        #Menu.

    def menu(self):
        userInput=0
        while userInput!='5':
            userInput=input("Select: ")

            if (userInput=='1'):
                element1="x9"
                while ((ord(element1[0]) < 97) or (ord(element1[0]) > (96 + size)) or
                       (int(element1[1]) < 0) or (int(element1[1]) > size - 1)):  # Validating cell coordinates.

                    element1 = input("Enter cell coordinates (e.g., a0): ").lower()
                    if ((ord(element1[0]) < 97) or (ord(element1[0]) > (96 + size)) or
                            (int(element1[1]) < 0) or (int(element1[1]) > size - 1)):
                        print("input error: row entry is out of range for this grid. Please try again.")

                element2="x9"
                while ((ord(element2[0]) < 97) or (ord(element2[0]) > (96 + size)) or
                       (int(element2[1]) < 0) or (int(element2[1]) > size - 1) or
                       element1 == element2):  # Validating cell coordinates for element 2.

                    element2 = input("Enter cell coordinates (e.g., b0): ").lower()
                    if ((ord(element2[0]) < 97) or (ord(element2[0]) > (96 + size)) or
                            (int(element2[1]) < 0) or (int(element2[1]) > size - 1) or
                            element1 == element2):
                        print("input error: row entry is out of range for this grid. Please try again.")

                #os.system("cls")
                index1=((size*int(element1[1])) + (ord(element1[0])-97))
                index2=((size*int(element2[1])) + (ord(element2[0])-97))


                if(not gridX.checkCell(index1,index2)):
                    gridX.updateCell(index1,index2)
                    self.printScreen(False)
                    time.sleep(2)
                    gridX.switchBacktoHide(index1,index2)
                    self.printScreen(False)


                #gridX.updateCell(index1,index2)
                # do this
            elif(userInput=='2'):
                index1 = "x9"
                visibilityflag=True

                while ((ord(index1[0]) < 97) or (ord(index1[0]) > (96 + size)) or
                       (int(index1[1]) < 0) or (int(index1[1]) > size - 1) or
                visibilityflag):  # Validating cell coordinates for element 2.

                    index1 = input("Enter cell coordinates (e.g., a0): ").lower()
                    intIndex1 = ((size * int(index1[1])) + (ord(index1[0]) - 97))


                    if ((ord(index1[0]) < 97) or (ord(index1[0]) > (96 + size)) or
                       (int(index1[1]) < 0) or (int(index1[1]) > size - 1)):
                        print("input error: row entry is out of range for this grid. Please try again.")

                    elif (gridX.checkVisibility(intIndex1)):
                        print("input error: element is already visible! ")

                    else:
                        visibilityflag=False
                        gridX.unCoverCell(intIndex1)
                        self.printScreen(False)

                # do this
            elif(userInput=='3'):
                gridX.revealGrid()
                self.printScreen(False)
                userInput='5'
                # do this
            elif(userInput=='4'):
                #TODO score reset.
                gridX.resetGame()
                gridX.randArray()
                self.printScreen()
            #os.system("cls")
            self.printScreen()
                #do this


#os.system("cls")
myinstance = Main()
myinstance.printScreen()
myinstance.menu()


