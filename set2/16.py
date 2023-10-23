from math import isqrt

def sumOfDigits(number):
    sum = 0
    while 0 != number:
        sum += number % 10
        number //= 10
    #end while
    return sum

def isPrime(number):
    if number == 1 or number == 0:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        div = 3
        iroot = isqrt(number)
        while div <= iroot:
            if number % div == 0:
                return False
            div += 2
        #end while
    #end if

    return True

def isSmithNumber(number):
    if isPrime(number):
        return False

    mySumOfDigits = sumOfDigits(number)
    sumOfDivsDigits = 0

    while number % 2 == 0:
        sumOfDivsDigits += 2
        number //= 2
    #end while
    
    div = 3
    isMaxDiv = False

    while (not isMaxDiv) and (1 != number):
        iroot = isqrt(number)

        while number % div == 0:
            sumOfDivsDigits += sumOfDigits(div)
            number //= div
        #end while

        updatedDiv = False
        while not updatedDiv:
            div += 2

            if div > iroot:
                isMaxDiv = True
                updatedDiv = True

            if isPrime(div):
                updatedDiv = True
        #end while
    #end while

    if 1 != number:
        sumOfDivsDigits += sumOfDigits(number)
    
    return mySumOfDigits == sumOfDivsDigits

if __name__ == "__main__":
    assert(sumOfDigits(123) == 6)
    assert(isPrime(7))
    for number in range(1, 1000000):
        if (isSmithNumber(number)):
            print(number)