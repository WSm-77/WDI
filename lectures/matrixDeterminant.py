def matrixDeterminant(matrix):
    matrixSize = len(matrix)
    if matrixSize == 1:
        return matrix[0][0]
    #end if
    determinant = 0
    sign = 1
    for collumn in range(matrixSize):
        smallerMatrix = makeMatrix(matrix, matrixSize, collumn)
        determinant += sign * matrix[0][collumn] * matrixDeterminant(smallerMatrix)
        sign = -sign
    #end for
    return determinant
        
def makeMatrix(biggerMatrix, matrixSize, collumn):
    smallerMatrix = [[0 for _ in range(matrixSize - 1)] for _ in range(matrixSize - 1)]
    rowIncrement = -1
    for row in range(1, matrixSize):
        collumnIncrement = 0
        for coll in range(matrixSize):
            if coll == collumn:
                collumnIncrement = -1
                continue
            #end if
            smallerMatrix[row + rowIncrement][coll + collumnIncrement] = biggerMatrix[row][coll]
        #end for
    #end for
    return smallerMatrix

if __name__ == "__main__":
    matrix = [[1,2,3,1,1],
              [2,5,6,1,1],
              [7,8,-9,1,1],
              [10,11,12,13,1],
              [14,15,16,17,1]]
    
    # print(*makeMatrix(matrix, len(matrix), 1), sep='\n')
    print(matrixDeterminant(matrix))