
# increment 1 - if we add -1 - if we subtract
def updateDivsToTab(divs, number, increment):
    assert(number > 1)
    div = 2
    while 1 != number:
        while number % div == 0:
            divs[div] += increment
            number //= div
        #end while
        div += 1
    return divs

def maxLen(numArray):
    divs = [0 for _ in range(1000)]
    arrayLen = len(numArray)
    myMaxLen = 0
    windowStart = 0
    windowLen = 1
    while windowStart + windowLen - 1 < arrayLen:
        windowEnd = windowStart + windowLen - 1
        currentLen = 0
        while windowEnd < arrayLen:
            divs = updateDivsToTab(divs, numArray[windowEnd], 1)
            if max(divs) > 1:
                break
            #end if
            windowLen = windowEnd - windowStart + 1
            currentLen += 1
            myMaxLen = max(myMaxLen, currentLen)
            windowEnd += 1
        #end while
        divs = updateDivsToTab(divs, numArray[windowStart], -1)
        windowStart += 1
        #end if
    #end while
    return myMaxLen

if __name__ == "__main__":
    numArray = [2,23,33,35,7,4,6,7,5,11,13,22]
    print(maxLen(numArray))