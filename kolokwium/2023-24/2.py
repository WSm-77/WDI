def valid_row(T, R):
    mySum = 0
    for i in range(9):
        mySum += T[R][i]
    #end for
    return mySum == 45      # 1+2+3+4+5+6+7+8+9=45

def valid_collumn(T, C):
    mySum = 0
    for i in range(9):
        mySum += T[i][C]
    #end for
    return mySum == 45      # 1+2+3+4+5+6+7+8+9=45

def valid(T, RorC, constRow=True):
    RC = None
    if constRow:
        rowIterator = multiplicity(0)
        collIterator = multiplicity(1)
        RC = (RorC, 0)
    else:
        rowIterator = multiplicity(1)
        collIterator = multiplicity(0)
        RC = (0, RorC)
    #end if
    mySum = 0
    for i in range(9):
        mySum += T[RC[0] + rowIterator(i)][RC[1] + collIterator(i)]
    #end for
    return mySum == 45
        

def multiplicity(i):
    return lambda x: x * i

if __name__ == "__main__":
    correctsudoku= [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    
    print(valid_row(correctsudoku,0))
    print(valid_collumn(correctsudoku,0))
    print(valid(correctsudoku, 0))
    print(valid(correctsudoku, 2, False))
