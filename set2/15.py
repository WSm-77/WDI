# this program searches for numbers which has uniqe property that sum of N-th power of it's digits is equal to this number
# N is length of this number

from math import log10

# this function returns digit value at specifis index
# e.g. for number = 1 2 3 4 5 at index 2 it will return 3
#                       ^   ^
#                       |   |
# index:            4 3 2 1 0
def currentDigitValue(number, index):
    return number % (10 ** (index + 1)) // (10 ** index)

def buildNumbers(numLength):
    number = 10 ** (numberLen - 1)
    # number = 0

    # power = 1
    # for _ in range(numLength):
    #     number += 1 * power
    #     power *= 10
    #end for

    currentIndex = 0
    currentDigit = 1
    reachedEnd = False
    sumNthPower = 0

    while not reachedEnd:
        lastDigit = number % 10
        while lastDigit < 9:
            sumNthPower = sumDigitsNthPower(number, numberLen)
            if numberLength(sumNthPower) == numberLen:
                if sameDigital(number, sumNthPower):
                    print("number:", sumNthPower)        # there we print our numbers
            lastDigit += 1
            number += 1
        else:
            sumNthPower = sumDigitsNthPower(number, numberLen)
            if numberLength(sumNthPower) == numberLen:
                if sameDigital(number, sumNthPower):
                    print("number:", sumNthPower)        # there we print our numbers
        # end while

        # update index
        updatedIndex = False
        while not updatedIndex:
            currentIndex += 1
            if currentIndex == numLength:
                reachedEnd = True
                updatedIndex = True
            #end if

            currentDigit = currentDigitValue(number, currentIndex)

            if currentDigit < 9:
                currentDigit += 1

                # this cuts number from current index to 0 index
                # e.g. from 12399 it makes 12000 
                #             ^
                #             |
                #          currentIndex
                number = number - (number % (10 ** (currentIndex + 1)))
                # fill rest number with currentDigit
                # e.g 12444
                for p in range(currentIndex, -1, -1):
                    number += currentDigit * (10 ** (p))
                #end while 
                currentIndex = 0
                updatedIndex = True
            #end if
        #end while
    #end while

def sumDigitsNthPower(number, numberLen):
    sum = 0
    while 0 != number:
        sum += (number % 10) ** (numberLen)
        number //= 10
    #end while
    return sum

def numberLength(number):
    return int(log10(number)) + 1

def sameDigital(firstNum, secondNum):
    mySameDigital = True
    while 0 != firstNum:
        lastDigit = firstNum % 10
        index = 0
        while 10**index <= secondNum:
            if currentDigitValue(secondNum, index) == lastDigit:
                secondNumHalf = secondNum % (10**(index))
                secondNum = (secondNum - (secondNum % 10**(index + 1))) // 10 + secondNumHalf
                break
            #end if
            index += 1
        else:
            mySameDigital = False
            break
        #end while
        firstNum //= 10
    #end while
    return mySameDigital


if __name__ == "__main__":
    numberLen = int(input("enter number length: "))
    assert(sameDigital(123,321))
    assert(sameDigital(12244,41224))
    assert(sameDigital(12,34) == False)
    # print("yes")
    buildNumbers(numberLen)
