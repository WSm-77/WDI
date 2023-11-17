def valid_row_and_coll(T, ele):
    myRowSum = 0
    myCollSum = 0
    for i in range(9):
        myRowSum += T[ele][i]
        myCollSum += T[i][ele]
    #end for
    return myRowSum == myCollSum == 45      # 1+2+3+4+5+6+7+8+9=45

def compareSmallSqRowAndColl(sudo, currR, currC, validIndex):
    
    for elementRow in range(3):
        currentRow = 3 * currR + elementRow
        for elementColl in range(3):
            curretnColl = 3 * currC + elementColl
            currentNum = sudo[currentRow][curretnColl]
            for iterator in range(3):
                if currentNum == sudo[currentRow][3 * validIndex + iterator] or \
                currentNum == sudo[3 * validIndex + iterator][curretnColl]:
                    return False
                #end if
            #end for
        #end for
    #end for
    return True

def sudoku(sudo):
    incorrectSmallSq =[0,0]
    incorrectSqIndex = 0
    validSmallSqRow = [False for _ in range(3)]
    validSmallSqColl = [False for _ in range(3)]
    validSmallSqRowAndCollIndex = 0
    for diagonalSmallSq in range(3):
        validSmallSq = True
        for element in range(3):
            if not valid_row_and_coll(sudo, 3 * diagonalSmallSq + element):
                validSmallSq = False
                break
        #end for
        if validSmallSq:
            validSmallSqRow[diagonalSmallSq] = True
            validSmallSqColl[diagonalSmallSq] = True
            validSmallSqRowAndCollIndex = diagonalSmallSq
            break
    #end for

    for smallSqRowIndex in range(3):
        if validSmallSqRow:
            continue
        #end if
        for smallSqCollIndex in range(3):
            if validSmallSqColl:
                continue
            #end if
            if not compareSmallSqRowAndColl(sudo, smallSqRowIndex, smallSqCollIndex, validSmallSqRowAndCollIndex):
                incorrectSmallSq[incorrectSqIndex] = 3 * smallSqRowIndex + smallSqCollIndex + 1
                incorrectSqIndex += 1
                if incorrectSqIndex > 1:
                    return tuple(incorrectSmallSq)
                #end if
            #end if
        #end for
    #end for
    return (0,0)

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
    
    # print(valid_row_and_coll(correctsudoku, 1, 2))
    # print(sudoku(correctsudoku))
    
    wrongsudoku =  [[5, 3, 4,   6, 7, 8,    9, 1, 2],
                    [6, 7, 2,   1, 9, 5,    3, 4, 8],
                    [1, 9, 8,   3, 4, 2,    5, 6, 7],

                    [8, 5, 9,   2, 8, 4,    4, 2, 3],
                    [4, 2, 6,   6, 3, 5,    7, 9, 1],
                    [7, 1, 3,   1, 7, 9,    8, 5, 6],

                    [9, 6, 1,   5, 3, 7,    7, 6, 1],
                    [2, 8, 7,   4, 1, 9,    8, 5, 3],
                    [3, 4, 5,   2, 8, 6,    9, 2, 4]]
    
    print(compareSmallSqRowAndColl(wrongsudoku, 0, 2, 1))
    print(valid_row_and_coll(wrongsudoku, 3))
    # print(sudoku(wrongsudoku))
