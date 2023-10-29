def gcd(firstNum, secondNum):
    while 0 != firstNum:
        firstNum, secondNum = secondNum % firstNum, firstNum
    return secondNum

def tripletsCounter(numArray):
    arrayLen = len(numArray)
    cntr = 0
    firstPtr = 0
    while firstPtr < arrayLen - 2:
        secondPtr = firstPtr + 1
        while secondPtr - firstPtr <= 2 and secondPtr < arrayLen - 1:
            thirdPtr = secondPtr + 1
            while thirdPtr - secondPtr <= 2 and thirdPtr < arrayLen:
                if gcd(gcd(numArray[firstPtr], numArray[secondPtr]), numArray[thirdPtr]):
                    cntr += 1
                    # print(numArray[firstPtr], numArray[secondPtr], numArray[thirdPtr])        # this prints all triplets
                #end if
                thirdPtr += 1
            #end while
            secondPtr += 1
        #end while
        firstPtr += 1
    #end while
    return cntr


if __name__ == "__main__":
    numArray = [1,2,3,5,7,11]
    print(tripletsCounter(numArray))