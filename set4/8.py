def geometricSeriesLen(tab, rowStart, collStart):
    tabLen = len(tab)
    assert(tabLen > 2)
    quotient = round(tab[rowStart + 1][collStart + 1] / tab[rowStart][collStart], 5)
    maxLen = 2
    currentLen = 2
    rowStart += 1
    collStart += 1
    while rowStart < tabLen - 1 and collStart < tabLen - 1:
        currentQotient = round(tab[rowStart + 1][collStart + 1] / tab[rowStart][collStart], 5)
        if  currentQotient == quotient:
            currentLen += 1
            maxLen = max(maxLen, currentLen)
        else:
            currentLen = 2
            quotient = currentQotient
        #end if
        rowStart += 1
        collStart += 1
    #end while
    return maxLen
#end def

def longestGeometricSeries(tab):
    tabLen = len(tab)
    maxSeriesLen = geometricSeriesLen(tab, 0, 0)
    for start in range(1, tabLen - 2):
        maxSeriesLen = max(maxSeriesLen, geometricSeriesLen(tab, start, 0), geometricSeriesLen(tab, 0, start))
    #end for
    if maxSeriesLen < 3:
        print("not found")
    else:
        print("longest series len:", maxSeriesLen)

    #end if
#end def

if __name__ == "__main__":
    tab = [[1,81,3,4,5],
           [1,4,27,5,5],
           [1,1,1,9,7],
           [1,5,2,4,3],
           [1,1,1,1,1]]
    
    longestGeometricSeries(tab)

    tab = [[1,2,3,4,5,32],
           [1,4,4,5,5,32],
           [1,1,16,8,7,32],
           [1,5,1,64,16,32],
           [1,1,1,1,256,32],
           [2,3,4,5,1,1024]]
    
    longestGeometricSeries(tab)