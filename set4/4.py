def collumnToRowSumMaxQotient(tab):
    tabLen = len(tab)
    # rowsSums = [0 for _ in range(tabLen)]
    # collumnsSums = [0 for _ in range(tabLen)]
    rowIndex = 0
    collumnIndex = 0
    rowsMinSum = 0
    collumnsMaxSum = 0
    for row in range(tabLen):
        currentRowSum = 0
        currentCollumnSum = 0
        for collumn in range(tabLen):
            currentRowSum += tab[row][collumn]
            currentCollumnSum += tab[collumn][row]
        #end for
        # rowsSums[row] = currentRowSum
        # collumnsSums[row] = currentCollumnSum
        if currentCollumnSum > collumnsMaxSum or row == 0:
            collumnsMaxSum = currentCollumnSum
            collumnIndex = row
        if currentRowSum < rowsMinSum or row == 0:
            rowsMinSum = currentRowSum
            rowIndex = row
    #end for
    # print("collumnsSums:",collumnsSums)
    # print("rowsSums:", rowsSums)
    return collumnIndex, rowIndex

if __name__ == "__main__":
    tab = [[62,13,4,2],
           [24,27,12,4],
           [3,42,2,2],
           [24,135,8,2]]
    
    print("column index, row index:", collumnToRowSumMaxQotient(tab))

    tab =   [[1, 2, 3, 4, 5, 6, 7],
            [24, 25, 26, 27, 28, 29, 8],
            [23, 40, 41, 42, 43, 30, 9],
            [22, 39, 48, 49, 44, 31, 10],
            [21, 38, 47, 46, 45, 32, 11],
            [20, 37, 36, 35, 34, 33, 12],
            [19, 18, 17, 16, 15, 14, 13]]
    
    print("column index, row index:", collumnToRowSumMaxQotient(tab))