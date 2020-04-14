# Sudoku game
import random




numberTable = [[0, 0, 0,  0, 0, 0,  0, 0, 0],
               [0, 0, 0,  0, 0, 0,  0, 0, 0],
               [0, 0, 0,  0, 0, 0,  0, 0, 0],

               [0, 0, 0,  0, 0, 0,  0, 0, 0],
               [0, 0, 0,  0, 0, 0,  0, 0, 0],
               [0, 0, 0,  0, 0, 0,  0, 0, 0],

               [0, 0, 0,  0, 0, 0,  0, 0, 0],
               [0, 0, 0,  0, 0, 0,  0, 0, 0],
               [0, 0, 0,  0, 0, 0,  0, 0, 0]]

def rowCheck(row, number):
    if number not in numberTable[row]:
        return True
    else:
        return False


def columnCheck(ind, number):
    for i in range(9):
        if number == numberTable[i][ind]:
            return False
    return True

def origoSwitch(row, column):
    pass

def regionCheck(origo,column, number):
    #if (row % 3) == 0: #and (column % 3) == 0:
    for i in range(3):
        for j in range(3):
                #print(origo+i)
            if number == numberTable[origo+i][column+j]:
                return False
    return True



for row in range(9):
        restart = True
        while restart:
            for i in range(9):
                numberTable[row][i] = 0
            count = 0
            for column in range(9):
                loopCount = 0
                while numberTable[row][column] == 0:
                    loopCount += 1

                    number = random.randrange(1, 10 , 1)
                    if row < 3 and column < 3:
                        indOne = 0
                        indTwo = 0
                    elif row < 3 and 2 < column < 6:
                        indOne = 0
                        indTwo = 3
                    elif row < 3 and column > 5:
                        indOne = 0
                        indTwo = 6
                    elif 2 < row < 6 and column < 3:
                        indOne = 3
                        indTwo = 0
                    elif 2 < row < 6 and 2 < column < 6:
                        indOne = 3
                        indTwo = 3
                    elif 2 < row < 6 and 5 < column:
                        indOne = 3
                        indTwo = 6
                    elif 5 < row and column < 3:
                        indOne = 6
                        indTwo = 0
                    elif 5 < row and 2 < column < 6:
                        indOne = 6
                        indTwo = 3
                    elif 5 < row and 5 < column:
                        indOne = 6
                        indTwo = 6


                    if rowCheck(row, number) and columnCheck(column, number) and regionCheck(indOne, indTwo, number):
                        numberTable[row][column] = number
                        count += 1
                    if count == 9:
                        restart = False
                    elif loopCount > 100 and count < 9:
                        break

                    print(f"\n   loop:{loopCount}    column: {column}             Debug Table     {number}             ")
                    for g in range(9):
                        if (g % 3) == 0:
                            print("\n")
                        print(numberTable[g])
                    print(count)





print("\n                    Final Table                  ")
for i in range(9):
    if (i % 3) == 0:
        print("\n")
    print(numberTable[i])
