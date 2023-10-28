# from random import randint
from math import isqrt

def isPrime(number):
    if number == 2:
        return True
    elif number < 2 or number % 2 == 0:
        return False
    else:
        div = 3
        iroot = isqrt(number)
        while div <= iroot:
            if number % div == 0:
                return False
            else:
                div += 2
            #end if
        #end while
        return True
    #end if

##################
# first solution #
##################

# this solution is not optimal

def correctSumsBit(firstArray, secondArray):
    n = len(firstArray)
    correctSumsCntr = 0
    primeSumsCntr = 0
    numberOfBitMasks = 2**(n)
    usedEveryIndex = numberOfBitMasks - 1
    for firstBitMask in range(numberOfBitMasks):
        for secondBitMask in range(numberOfBitMasks):
            if (firstBitMask | secondBitMask) != usedEveryIndex:
                continue
            #end if
            print(f"firstBitMask: {firstBitMask}, secondBitMask: {secondBitMask}")
            correctSumsCntr += 1
            myCorrectSum = 0
            firstBitMaskCp = firstBitMask
            secondBitMaskCp = secondBitMask
            for i in range(n):
                myCorrectSum += (firstBitMaskCp % 2) * firstArray[i]
                myCorrectSum += (secondBitMaskCp % 2) * secondArray[i]
                firstBitMaskCp //= 2
                secondBitMaskCp //= 2
            #end for
            print(f"{correctSumsCntr}. sum: {myCorrectSum}")
            if isPrime(myCorrectSum):
                print("prime")
                primeSumsCntr += 1
        #end for
    #end for
    return correctSumsCntr, primeSumsCntr

###################
# second solution #
###################

#trit mask: 0 - element from first array, 1 - eleme from second list, 2 - element form first and second list 

def correctSumsTrit(firstArray, secondArray):
    n = len(firstArray)
    correctSumsCntr = 0
    primeSumsCntr = 0
    tritMaskLen = 3**(n)
    for tritMask in range(tritMaskLen):
        myCorrectSum = 0
        for i in range(n):
            if tritMask % 3 == 0:
                myCorrectSum += firstArray[i]
            elif tritMask % 3 == 1:
                myCorrectSum += secondArray[i]
            else:
                myCorrectSum += firstArray[i] + secondArray[i]
            tritMask //= 3
            #end if
        #end for
        correctSumsCntr += 1
        print(f"{correctSumsCntr}. sum: {myCorrectSum}")
        if isPrime(myCorrectSum):
            print("prime")
            primeSumsCntr += 1
        #end if
    #end for
    return correctSumsCntr, primeSumsCntr


if __name__ == "__main__":
    # arrayLen = int(input("enter array length: "))
    # firstArray = [randint(1, 100) for _ in range(arrayLen)]
    # secondArray = [randint(1, 100) for _ in range(arrayLen)]
    # print(firstArray)
    # print(secondArray)
    firstArray = [1,2]
    secondArray = [9,4]
    # print(correctSumsBit(firstArray, secondArray))
    print(correctSumsTrit(firstArray, secondArray))
    firstArray = [1, 3, 2, 4]
    secondArray =  [9, 7, 4, 8]
    print(correctSumsTrit(firstArray, secondArray))
    # print(correctSumsBit(firstArray, secondArray))