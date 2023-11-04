##################
# first solution #
##################

def isEveryWhereZero(zeroInRows, zeroInColls):
    tabLen = len(zeroInColls)
    result = True
    for i in range(tabLen):
        if (zeroInColls[i] == False) or (zeroInRows[i] == False):
            result = False
            break
        #end if
    #end for
    return result

def zeroInEveryCollAndRow(tab):
    tabLen = len(tab)
    zeroInRows = [False for _ in range(tabLen)]
    zeroInColls = [False for _ in range(tabLen)]
    for row in range(tabLen):
        for coll in range(tabLen):
            if tab[row][coll] == 0:
                zeroInColls[coll] = True
                zeroInRows[row] = True
            #end if
        #end for
    #end for
    
    return True if isEveryWhereZero(zeroInRows, zeroInColls) else False

###################
# second solution #
###################

def zeroInEveryCollAndRowV2(tab):
    tabLen = len(tab)
    isZero = True
    for rowColl in range(tabLen):
        isInRow = False
        for row in range(tabLen):
            if tab[row][rowColl] == 0:
                isInRow = True
            #end if
        #end for
        if not isInRow:
            isZero = False
            break
        #end if
        isInColl = False
        for coll in range(tabLen):
            if tab[rowColl][coll] == 0:
                isInColl = True
            #end if
        #end for
        if not isInColl:
            isZero = False
            break
        #end if
    #end for
    
    return isZero

if __name__ == "__main__":
    tab = [[1,0,3,4,5],
           [1,4,27,0,5],
           [1,1,0,9,7],
           [0,5,2,4,3],
           [1,1,1,1,0]]
    
    print("version 1:",zeroInEveryCollAndRow(tab))
    print("version 2:", zeroInEveryCollAndRowV2(tab))

    tab = [[1,0,3,4,5],
           [1,4,27,0,5],
           [1,1,0,9,7],
           [1,5,2,4,3],
           [1,1,1,1,0]]
    
    print("version 1:",zeroInEveryCollAndRow(tab))
    print("version 2:", zeroInEveryCollAndRowV2(tab))

    tab = [[0,0,3,4,5],
           [1,4,0,0,0],
           [1,1,0,9,7],
           [0,5,0,4,3],
           [1,0,1,1,0]]
    
    print("version 1:",zeroInEveryCollAndRow(tab))
    print("version 2:", zeroInEveryCollAndRowV2(tab))