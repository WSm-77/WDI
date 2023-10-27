from random import randint

def longestArithmeticSeq(numArray, arrayLen):
    assert(arrayLen > 1)
    maxArithmeticSeqLength = 2
    currentArithmeticSeqLength = 2
    seqDifference = numArray[1] - numArray[0]

    for i in range(1, arrayLen - 1):
        currentDifference = numArray[i + 1] - numArray[i]

        if currentDifference == seqDifference:
            currentArithmeticSeqLength += 1
            maxArithmeticSeqLength = max(maxArithmeticSeqLength, currentArithmeticSeqLength)
        else:
            seqDifference = currentDifference
            currentArithmeticSeqLength = 2
        #end if
    #end for

    return maxArithmeticSeqLength

if __name__ == "__main__":
    assert(longestArithmeticSeq([1,2,3,4,5,6,7,8,9,10], 10) == 10)
    assert(longestArithmeticSeq([1,2,3,1,4,5,6,7,8,9,10,2], 12) == 7)
    assert(longestArithmeticSeq([3,2,1,6,4,2,0,-2,1,4,6,3,7,1], 14) == 5)
    arrayLen = int(input("enter array length: "))
    numArray = [randint(1, 10) for _ in range(arrayLen)]
    print(numArray)
    print(longestArithmeticSeq(numArray, arrayLen))