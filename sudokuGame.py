# Sudoku game
import random

row = [0, 1, 2, 3, 4, 5, 6, 7, 8]
collums =
cell =


numberTable = [[0, 0, 0,  0, 0, 0,  0, 0, 0],
               [0, 0, 0,  0, 0, 0,  0, 0, 0],
               [0, 0, 0,  0, 0, 0,  0, 0, 0],

               [0, 0, 0,  0, 0, 0,  0, 0, 0],
               [0, 0, 0,  0, 0, 0,  0, 0, 0],
               [0, 0, 0,  0, 0, 0,  0, 0, 0],

               [0, 0, 0,  0, 0, 0,  0, 0, 0],
               [0, 0, 0,  0, 0, 0,  0, 0, 0],
               [0, 0, 0,  0, 0, 0,  0, 0, 0]]


for j in range(9):
        count = 0
        while 0 in numberTable[j]:
            number = random.randrange(1, 10 , 1)
            if number not in numberTable[j]:
                numberTable[j][count] = number
                count += 1







for i in range(9):
    if (i % 3) == 0:
        print("\n")
    print(numberTable[i])
