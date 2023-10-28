from random import randint
from math import ceil

def subarrayWithItsReversLen(numArray, arrayLen):
    maxLen = 1
    currentLen = 1
    firstWindowStart = 0
    for firstWindowEnd in range(1, ceil(arrayLen/2)):
        currentLen = firstWindowEnd - firstWindowStart + 1
        foundRevers = False
        for secondWindowStart in range(arrayLen - 1, firstWindowEnd - 1, -1):
            if numArray[secondWindowStart] != numArray[firstWindowStart]:
                continue
            #end if
            foundRevers = True
            for iterator in range(currentLen):
                if numArray[firstWindowStart + iterator] != numArray[secondWindowStart - iterator]:
                    foundRevers = False
                    break
                #end if
            #end for
            if foundRevers:
                break
        #end for
        if foundRevers:
            maxLen = max(maxLen, currentLen)
        else:
            firstWindowStart = firstWindowEnd
        #end if
    #end for
    return maxLen

if __name__ == "__main__":
    testArray = [1,2,2,3,4,1,3,2,2,1,0]
    assert(subarrayWithItsReversLen(testArray, len(testArray)) == 4)
    testArray = [1,2,3,0,0,12,3,2,1,2,1]
    assert(subarrayWithItsReversLen(testArray, len(testArray)) == 3)
    arrayLen = int(input("enter array length: "))
    numArray = [randint(1, 3) for _ in range(arrayLen)]
    print(numArray)
    print(subarrayWithItsReversLen(numArray, arrayLen))