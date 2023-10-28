def isOdd(number):
    return number % 2 == 1

def oddPalindromLength(numArray, leftIndex, rightIndex):
    arrayLen = len(numArray)
    paliLen = 0
    i = 0
    while leftIndex - i >= 0 and rightIndex + i < arrayLen:
        if numArray[leftIndex - i] != numArray[rightIndex + i]:
            break
        elif isOdd(numArray[leftIndex - i]):
            paliLen += 2
        else:
            break
        #end if
        i += 1
    #end while
    # print(numArray[leftIndex - i + 1: rightIndex + i])        # this prints current palindrom
    return paliLen

def solution(numArray):
    arrayLen = len(numArray)
    maxLen = 0
    
    for leftIndex in range(arrayLen - 1):
        if not isOdd(numArray[leftIndex]):
            continue
        #end if
        currentPaliLen = 1
        rightIndex = leftIndex + 1
        while rightIndex < arrayLen:
            if numArray[rightIndex] == numArray[rightIndex - 1]:
                rightIndex += 1
                currentPaliLen += 1
            else:
                break
            #end if
        #end while
        currentPaliLen += oddPalindromLength(numArray, leftIndex - 1, rightIndex)
        maxLen = max(maxLen, currentPaliLen)
        #end if
    #end for
    return maxLen

if __name__ == "__main__":
    numArray = [2,4,5,3,1,3,5]
    print(solution(numArray))

    numArray = [2,4,5,3,1,1,3,5]
    print(solution(numArray))

    numArray = [2,4,3,1,3,5,3,1,3,5]
    print(solution(numArray))

    numArray = [3,3,4,4,4,4,4]
    print(solution(numArray))

    numArray = [4,4,4,4,3,3,3]
    print(solution(numArray))

    numArray = [4,4,4,4]
    print(solution(numArray))