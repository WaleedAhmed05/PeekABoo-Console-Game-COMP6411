
from grid import grid

class main:

    def printScreen(self):
        print("---------------------\n"
              "|    PEEK-A-BOO     |\n"
              "---------------------\n")
        grid.blankGrid(4)
        print("Here's grid X\n") #this will print grid.
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
                print("1")
                # do this
            elif(userInput=='2'):
                print("1")
                # do this
            elif(userInput=='3'):
                print("1")
                # do this
            elif(userInput=='4'):
                print("1")
                #do this



myinstance = main()
myinstance.printScreen()
myinstance.menu()


