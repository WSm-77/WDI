def findNotReached(reachedEnd):
    notReached = 0
    while reachedEnd[notReached]:
        notReached += 1
    #end while
    return notReached

def findMinIndex(tab, collumIndexesTab, reachedEnd):
    indexTabLen = len(collumIndexesTab)
    isUniqe = False
    minIndex = 0
    while not isUniqe and not everyReachedEnd(reachedEnd):
        minIndex = findNotReached(reachedEnd)
        isUniqe = True
        notUniqeNumber = 0
        for rowIndex in range(minIndex + 1, indexTabLen):
            if reachedEnd[rowIndex]:
                continue
            #end if
            currentNumber = tab[rowIndex][collumIndexesTab[rowIndex]]
            if currentNumber == tab[minIndex][collumIndexesTab[minIndex]]:
                isUniqe = False
                notUniqeNumber = currentNumber
            elif currentNumber < tab[minIndex][collumIndexesTab[minIndex]]:
                minIndex = rowIndex
                isUniqe = True
            #end if
        #end for

        #update not reached tab
        if not isUniqe:
            for updateIndex in range(minIndex, indexTabLen):
                if reachedEnd[updateIndex]:
                    continue
                #end if
                if notUniqeNumber != tab[updateIndex][collumIndexesTab[updateIndex]]:
                    continue
                #end if
                collumIndexesTab[updateIndex] += 1
                if collumIndexesTab[updateIndex] == indexTabLen:
                    reachedEnd[updateIndex] = True
                #end if
            #end for
        #end if
    #end while
    return minIndex

def everyReachedEnd(reachedEnd):
    everyReached = True
    for i in range(len(reachedEnd)):
        if not reachedEnd[i]:
            everyReached = False
            break
        #end if
    #end for
    return everyReached

def singletons(tab):
    tabLen = len(tab)
    tab2 = [0 for _ in range(tabLen*tabLen)]
    tab2Index = 0
    collumIndexesTab = [0 for _ in range(tabLen)]
    reachedEnd = [False for _ in range(tabLen)]
    while True:
        minElementRowIndex = findMinIndex(tab, collumIndexesTab, reachedEnd)
        if everyReachedEnd(reachedEnd):
            break
        #end if
        tab2[tab2Index] = tab[minElementRowIndex][collumIndexesTab[minElementRowIndex]]
        tab2Index += 1
        collumIndexesTab[minElementRowIndex] += 1
        if collumIndexesTab[minElementRowIndex] == tabLen:
            reachedEnd[minElementRowIndex] = True
    #end while
    return tab2

if __name__ == "__main__":
    tab = [[1,3,7],
           [4,7,8],
           [2,5,6]]
    
    print(singletons(tab))

    tab = [[1,2,7,10],
           [2,8,12,17],
           [7,16,20,24],
           [5,14,17,21]]

    print(singletons(tab))
    
    tab = [[1,4,7],
           [2,5,7],
           [3,6,7]]

    print(singletons(tab))