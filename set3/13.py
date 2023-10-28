from random import randint

def subarrayWithItsReversLen(numArray, arrayLen):
    maxLen = 1
    currentLen = 1
    firstWindowStart = 0
    for firstWindowEnd in range(1, arrayLen):
        # print(numArray[firstWindowStart:firstWindowEnd + 1])          # this prints current first window

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
            firstWindowStart += 1
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
    testArray = [2, 3, 2, 2, 3, 3, 1, 3, 2, 3]
    assert(subarrayWithItsReversLen(testArray, len(testArray)) == 4)
    testArray = [11,1,2,3,4,5,4,3,2,1,0,2]
    assert(subarrayWithItsReversLen(testArray, len(testArray)) == 9)
    print(numArray)
    print(subarrayWithItsReversLen(numArray, arrayLen))