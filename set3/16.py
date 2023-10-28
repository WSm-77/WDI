from random import randint

def doesExistUniqeMinAndMax(numArray):
    arrayLen = len(numArray)
    uniqeMax = uniqeMin = False
    maxElem = minElem = numArray[0]
    for i in range(1, arrayLen):
        currentNumber = numArray[i]
        if currentNumber == maxElem:
            uniqeMax = False
        elif currentNumber == minElem:
            uniqeMin = False
        elif currentNumber > maxElem:
            maxElem = currentNumber
            uniqeMax = True
        elif currentNumber < minElem:
            minElem = currentNumber
            uniqeMin = True
        #end if
    #end for
    return uniqeMin and uniqeMax


if __name__ == "__main__":
    numArray = [2,1,7,2,3,4,5,7]
    assert(not doesExistUniqeMinAndMax(numArray))
    numArray = [2,1,7,2,3,4,5,6]
    assert(doesExistUniqeMinAndMax(numArray))
    numArray = [2,1,7,2,3,1,5,6]
    assert(not doesExistUniqeMinAndMax(numArray))
    numArray = [randint(1,20) for _ in range(10)]
    print(numArray)
    print(doesExistUniqeMinAndMax(numArray))