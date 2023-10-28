def isOdd(number):
    return number % 2 == 1

def oddPalindromLength(numArray, leftIndex, rightIndex):
    arrayLen = len(numArray)
    paliLen = 0
    i = 0
    while leftIndex - i >= 0 and rightIndex + i < arrayLen:
        if numArray[leftIndex - i] == numArray[rightIndex + i]:
            if isOdd(numArray[leftIndex - i]):
                paliLen += 2
            else:
                break
            #end if
        #end if
        i += 1
    #end while
    return paliLen

def solution(numArray):
    arrayLen = len(numArray)
    maxLen = 0
    
    for i in range(arrayLen - 1):
        if isOdd(numArray[i]):
            currentPaliLen = 0
            if numArray[i] == numArray[i + 1]:
                currentPaliLen = oddPalindromLength(numArray, i, i + 1)
            else:
                currentPaliLen = oddPalindromLength(numArray, i - 1, i + 1) + 1
            #end if
            maxLen = max(maxLen, currentPaliLen)
        #end if
    #end for
    return maxLen

if __name__ == "__main__":
    numArray = [2,4,5,3,1,3,5]
    print(solution(numArray))
    numArray = [2,4,5,3,1,1,3,5]
    print(solution(numArray))
    numArray = [2,4,3,1,3,5,3,3,1,3,5]
    print(solution(numArray))
    numArray = [3,3,4,4,4,4,4]
    print(solution(numArray))
    numArray = [4,4,4,4,3,3,3]
    print(solution(numArray))