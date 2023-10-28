def maxLen(numArray):
    arrayLen = len(numArray)
    indexSum = 0
    risingElemsSum = 0
    myMaxLength = 0
    windowStart = 0
    windowLen = 2
    while windowStart + windowLen - 1 < arrayLen:
        indexSum = windowStart
        risingElemsSum = numArray[windowStart]
        currentRisingLen = 1
        for windowEnd in range(windowStart + windowLen - 1, arrayLen):
            if numArray[windowEnd] <= numArray[windowEnd - 1]:
                break
            #end if
            currentRisingLen += 1
            indexSum += windowEnd
            risingElemsSum += numArray[windowEnd]
            if indexSum == risingElemsSum:
                windowLen = windowEnd - windowStart + 1
                myMaxLength = max(myMaxLength, currentRisingLen)
            #end if
        #end for
        windowStart += 1
    #end while


    return myMaxLength


if __name__ == "__main__":
    numArray = [7,0,1,3,6,20,10]      # 0 + 1 + 3 + 6 = 1 + 2 + 3 + 4 = 10
    print(maxLen(numArray))

    numArray = [0,1,2,3,4,5,6,20,10]
    print(maxLen(numArray))

    numArray = [2,1,2,0,0,0,0,7,8,9]
    print(maxLen(numArray))