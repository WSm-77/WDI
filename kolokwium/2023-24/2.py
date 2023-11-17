def valid_row_and_coll(T, R, C):
    myRowSum = 0
    myCollSum = 0
    for i in range(9):
        myRowSum += T[R][i]
        myCollSum += T[i][C]
    #end for
    return myRowSum == myCollSum == 45      # 1+2+3+4+5+6+7+8+9=45

# def valid_row(T, R):
#     digits = [0 for _ in range(9)]
#     for i in range(9):
#         currentNum = T[R][i]
#         if digits[currentNum - 1] > 0:
#             return False
#         else:
#             digits[currentNum - 1] += 1
#         #end if
#     #end for
#     return True

# def valid_coll(T, C):
#     digits = [0 for _ in range(9)]
#     for i in range(9):
#         currentNum = T[i][C]
#         if digits[currentNum - 1] > 0:
#             return False
#         else:
#             digits[currentNum - 1] += 1
#         #end if
#     #end for
#     return True

def compareSmallSqRowAndColl(sudo, currR, currC, validRowIndex, validCollIndex):
    
    for elementRow in range(3):
        currentRow = 3 * currR + elementRow
        for elementColl in range(3):
            curretnColl = 3 * currC + elementColl
            currentNum = sudo[currentRow][curretnColl]
            for iterator in range(3):
                if currentNum == sudo[currentRow][3 * validCollIndex + iterator] or \
                currentNum == sudo[3 * validRowIndex + iterator][curretnColl]:
                    return False
                #end if
            #end for
        #end for
    #end for
    return True

def sudoku(sudo):
    incorrectSmallSq =[0,0]
    incorrectSqIndex = 0
    validSmallSqRowIndex = 0
    validSmallSqCollIndex = 0

    for curretnSmallSqRow in range(3):
        for currentSmallSqColl in range(3):
            validSmallSq = True
            for element in range(3):
                if not valid_row_and_coll(sudo, 3 * curretnSmallSqRow + element, 3 * currentSmallSqColl + element):
                    validSmallSq = False
                    break
            #end for
            if validSmallSq:
                validSmallSqRowIndex = curretnSmallSqRow
                validSmallSqCollIndex = currentSmallSqColl
                break
            #end if
        if validSmallSq:
            break
        #end for

    for smallSqRowIndex in range(3):
        if smallSqRowIndex == validSmallSqRowIndex:
            continue
        #end if
        for smallSqCollIndex in range(3):
            if smallSqCollIndex == validSmallSqCollIndex:
                continue
            #end if
            if not compareSmallSqRowAndColl(sudo, smallSqRowIndex, smallSqCollIndex, validSmallSqRowIndex, validSmallSqCollIndex):
                incorrectSmallSq[incorrectSqIndex] = 3 * smallSqRowIndex + smallSqCollIndex + 1
                incorrectSqIndex += 1
                if incorrectSqIndex > 1:
                    return tuple(incorrectSmallSq)
                #end if
            #end if
        #end for
    #end for
    print("this sudoku is correct")
    return (-1,-1)

if __name__ == "__main__":
    correctsudoku= [[5, 3, 4,   6, 7, 8,    9, 1, 2],
                    [6, 7, 2,   1, 9, 5,    3, 4, 8],
                    [1, 9, 8,   3, 4, 2,    5, 6, 7],

                    [8, 5, 9,   7, 6, 1,    4, 2, 3],
                    [4, 2, 6,   8, 5, 3,    7, 9, 1],
                    [7, 1, 3,   9, 2, 4,    8, 5, 6],

                    [9, 6, 1,   5, 3, 7,    2, 8, 4],
                    [2, 8, 7,   4, 1, 9,    6, 3, 5],
                    [3, 4, 5,   2, 8, 6,    1, 7, 9]]
    
    print(sudoku(correctsudoku))
    
    wrongsudoku =  [[5, 3, 4,   6, 7, 8,    9, 1, 2],
                    [6, 7, 2,   1, 9, 5,    3, 4, 8],
                    [1, 9, 8,   3, 4, 2,    5, 6, 7],

                    [8, 5, 9,   2, 8, 4,    4, 2, 3],
                    [4, 2, 6,   6, 3, 5,    7, 9, 1],
                    [7, 1, 3,   1, 7, 9,    8, 5, 6],

                    [9, 6, 1,   5, 3, 7,    7, 6, 1],
                    [2, 8, 7,   4, 1, 9,    8, 5, 3],
                    [3, 4, 5,   2, 8, 6,    9, 2, 4]]
    
    print(sudoku(wrongsudoku))

    wrongsudoku =  [[5, 3, 4,   7, 6, 1,    9, 1, 2],
                    [6, 7, 2,   8, 5, 3,    3, 4, 8],
                    [1, 9, 8,   9, 2, 4,    5, 6, 7],

                    [8, 5, 9,   6, 7, 8,    4, 2, 3],
                    [4, 2, 6,   1, 9, 5,    7, 9, 1],
                    [7, 1, 3,   3, 4, 2,    8, 5, 6],

                    [9, 6, 1,   5, 3, 7,    2, 8, 4],
                    [2, 8, 7,   4, 1, 9,    6, 3, 5],
                    [3, 4, 5,   2, 8, 6,    1, 7, 9]]
    
    print(sudoku(wrongsudoku))

    wrongsudoku =  [[5, 3, 4,   6, 7, 8,    9, 1, 2],
                    [6, 7, 2,   1, 9, 5,    3, 4, 8],
                    [1, 9, 8,   3, 4, 2,    5, 6, 7],

                    [8, 5, 9,   7, 6, 1,    4, 2, 3],
                    [4, 2, 6,   8, 5, 3,    7, 9, 1],
                    [7, 1, 3,   9, 2, 4,    8, 5, 6],

                    [5, 3, 7,   9, 6, 1,    2, 8, 4],
                    [4, 1, 9,   2, 8, 7,    6, 3, 5],
                    [2, 8, 6,   3, 4, 5,    1, 7, 9]]
    
    print(sudoku(wrongsudoku))