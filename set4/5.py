def collumnToRowSumMaxQotient(tab):
    tabLen = len(tab)
    posColIndex = posRowIndex = negColIndex = negRowIndex = 0
    maxPosCollSum = maxNegCollSum = 0
    minPosRowSum = minNegRowSum = 0
    rowsSums = [0 for _ in range(tabLen)]
    collumnsSums = [0 for _ in range(tabLen)]
    for row in range(tabLen):
        currentCollSum = 0
        currentRowSum = 0
        for collumn in range(tabLen):
            currentCollSum += tab[collumn][row]
            currentRowSum += tab[row][collumn]
        #end for
        rowsSums[row] = currentRowSum
        collumnsSums[row] = currentCollSum
        if currentRowSum > 0:
            if currentRowSum < minPosRowSum or minPosRowSum == 0:
                minPosRowSum = currentRowSum
                posRowIndex = row
            #end if
        #end if
        if currentRowSum < 0:
            if currentRowSum > minNegRowSum or minNegRowSum == 0:
                minNegRowSum = currentRowSum
                negRowIndex = row
            #end if
        #end if
        if currentCollSum > 0:
            if currentCollSum > maxPosCollSum or maxPosCollSum == 0:
                maxPosCollSum = currentCollSum
                posColIndex = row
            #end if
        #end if
        if currentCollSum < 0:
            if currentCollSum < maxNegCollSum or maxNegCollSum == 0:
                maxNegCollSum = currentCollSum
                negColIndex = row
            #end if
        #end if
    #end for
    print("collumnsSums:",collumnsSums)
    print("rowsSums:", rowsSums)
    if minPosRowSum == 0:
        return negColIndex, negRowIndex
    elif minNegRowSum == 0:
        return posColIndex, posRowIndex
    else:
        return (posColIndex, posRowIndex) if (maxPosCollSum / minPosRowSum) > (maxNegCollSum / minNegRowSum) else (negColIndex, negRowIndex)

if __name__ == "__main__":
    tab = [[62,-13,4,2],
           [24,27,-12,4],
           [-3,-42,2,2],
           [24,-135,8,-2]]
    
    print("column index, row index:", collumnToRowSumMaxQotient(tab))

    tab =   [[1, -2, 3, 4, 5, 6, 7],
            [-24, 25, 26, 27, 28, 29, 8],
            [23, -40, 41, -42, 43, -30, -9],
            [22, 39, 48, -49, -44, -31, 10],
            [21, -38, -47, 46, -45, -32, 11],
            [20, 37, 36, 35, 34, -33, 12],
            [19, -18, 17, -16, 15, -14, -13]]
    
    print("column index, row index:", collumnToRowSumMaxQotient(tab))