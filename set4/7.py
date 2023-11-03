def findMinElement(tab, collumnIndexTab):
    minRowIndex = -1
    minElement = 0
    tabLen = len(collumnIndexTab)
    for row in range(tabLen):
        if collumnIndexTab[row] == tabLen:
            continue
        #end if
        currentElement = tab[row][collumnIndexTab[row]]
        if currentElement < minElement or minRowIndex == -1:
            minElement = currentElement
            minRowIndex = row
        #end if
    #end for
    return minRowIndex

def fillSecondTabAscending(tab):
    tabLen = len(tab)
    collumnIndexTab = [0 for _ in range(tabLen)]
    tab2 = [0 for _ in range(tabLen*tabLen)]
    for tab2Index in range(tabLen*tabLen):
        minElementRow = findMinElement(tab, collumnIndexTab)
        tab2[tab2Index] = tab[minElementRow][collumnIndexTab[minElementRow]]
        collumnIndexTab[minElementRow] += 1
        #end if
    #end for
    return tab2

if __name__ == "__main__":
    tab = [[1,4,7],
           [2,5,7],
           [3,6,7]]
    
    print(fillSecondTabAscending(tab))

    tab = [[1,2,7,10],
           [2,8,12,17],
           [7,16,20,24],
           [5,14,17,21]]
    
    print(fillSecondTabAscending(tab))