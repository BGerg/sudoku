# Sudoku game
import random
import subprocess
import time


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


def columnCheck(column, number):
    for i in range(9):
        if number == numberTable[i][column]:
            return False
    return True

def regionCheck(origo,column, number):
    for i in range(3):
        for j in range(3):
            if number == numberTable[origo+i][column+j]:
                return False
    return True

def origoSwitch(row, column):
    if row < 3 and column < 3:
        indexRow = 0
        indexColumn = 0
    elif row < 3 and 2 < column < 6:
        indexRow = 0
        indexColumn = 3
    elif row < 3 and 5 < column :
        indexRow = 0
        indexColumn = 6
    elif 2 < row < 6 and column < 3:
        indexRow = 3
        indexColumn = 0
    elif 2 < row < 6 and 2 < column < 6:
        indexRow = 3
        indexColumn = 3
    elif 2 < row < 6 and 5 < column:
        indexRow = 3
        indexColumn = 6
    elif 5 < row and column < 3:
        indexRow = 6
        indexColumn = 0
    elif 5 < row and 2 < column < 6:
        indexRow = 6
        indexColumn = 3
    elif 5 < row and 5 < column:
        indexRow = 6
        indexColumn = 6

    return indexRow,indexColumn

def deleteRow(row):
    for i in range(9):
        numberTable[row][i] = 0

total = 0




proba = ""
for row in range(9):
        restart = True

        while restart:
            deleteRow(row)

            for column in range(9):
                loopCount = 0

                while numberTable[row][column] == 0:
                    loopCount += 1

                    number = random.randint(1, 9)
                    indexRow,indexColumn = origoSwitch(row, column)

                    if rowCheck(row, number) and columnCheck(column, number) and regionCheck(indexRow, indexColumn, number):
                        numberTable[row][column] = number
                        if column > 0 and numberTable[row][column-1] == 0 :
                            proba = "WTF"
                    if 0 not in numberTable[row]:
                        restart = False
                    elif loopCount > 10 and 0 in numberTable[row]:
                        break







                    print(f"\n    Debug Table  {proba}   Random number {number}             ")
                    for g in range(9):
                        if (g % 3) == 0:
                            print("\n")
                        print(numberTable[g])
                    
                    subprocess.call("clear")





print(f"\n    Total Loops: {total}                Final Table                  ")
for i in range(9):
    if (i % 3) == 0:
        print("\n")
    print(numberTable[i])
