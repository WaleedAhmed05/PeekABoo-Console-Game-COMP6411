import random


class Grid:
    #global rand_Array,rand_flag

    rand_Array=[] # list of random elements.
    rand_flag=[] # to maintain visibility of grid elements
    size=None


    def __init__(self, size):
        self.size = size


    def updateCell(self, index1, index2):
        self.rand_flag[index1]=True
        self.rand_flag[index2]=True

    def checkVisibility(self,index1): # check if given coordinate already visible?
        if(self.rand_flag[index1]):
            return True # return true if element is already visible
        else:
            return False

    def unCoverCell(self,index1):
        self.rand_flag[index1] = True

    def revealGrid(self):
        for i in range(len(self.rand_flag)):
            self.rand_flag[i]=True

    def resetGame(self):
        self.rand_Array.clear()
        self.rand_flag.clear()

    def  checkCell(self, index1, index2):
        if(self.rand_Array[index1]==self.rand_Array[index2]):
            self.rand_flag[index1] = True
            self.rand_flag[index2] = True
            return True
        else:
            return False
    def switchBacktoHide(self,index1,index2):
        self.rand_flag[index1] = False
        self.rand_flag[index2] = False

    def getrandFlag(self):
        return self.rand_flag


    def randArray(self):
        number_counts = {}  # Dictionary to maintain frequency of each element.
        while len(self.rand_Array) < self.size ** 2:  # Run until full grid size.
            random_number = random.randint(1, (self.size ** 2) / 2)
            if random_number not in number_counts:
                number_counts[random_number] = 1
                self.rand_Array.append(random_number)
                self.rand_flag.append(False)
            elif number_counts[random_number] < 2:
                number_counts[random_number] += 1
                self.rand_Array.append(random_number)
                self.rand_flag.append(False)

        # for i in range(size):
        #     for j in range(size):
        #         random_number = random.randint(1, (size ** 2) / 2)
        #         if random_number not in number_counts:
        #             number_counts[random_number] = 1
        #             rand_Array[i][j]=random_number
        #             rand_flag.append(False)
        #         elif number_counts[random_number] < 2:
        #             number_counts[random_number] += 1
        #             rand_Array[i][j]=random_number
        #             rand_flag.append(False)


    def blankGrid(self):
        for x in range(self.size):
            if (x == 0):
                print('  ', end=" ")
            print('[' + chr(x + 65) + ']', end="   ")  # print First row
        print(" ")

        counter=0
        for i in range(self.size):

            print(" \n")
            for j in range(self.size):
                if (j == 0):
                    print('[' + str(i) + ']', end=" ")  # print first column

                if(self.rand_flag[counter]):
                    #print(str(rand_Array[counter]), end="       ")
                    print('{:<5}'.format(str(self.rand_Array[counter])), end=" ")
                else:
                    #print("X", end="     ")
                    print('{:<5}'.format("X"), end=" ")
                counter+=1
            #print(" \n")


#print(ord('A'.lower()))

