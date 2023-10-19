from math import isqrt

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

def numberLen(number):
    if number == 0:
        return 1
    
    len = 0
    while 0 != number:
        number = number // 10
        len += 1
    #end while
    return len

# this function returns number of "1" bits in binary number
def numberOf1bits(bitNum):
    numOfOnes = 0
    while 0 != bitNum:
        numOfOnes = numOfOnes + (bitNum % 2)
        bitNum = bitNum // 2
    #end while
    return numOfOnes

def solution(firstNumber, secondNumber):
    firstNumLen = numberLen(firstNumber)
    secondNumLen = numberLen(secondNumber)
    targetNumberLen = firstNumLen + secondNumLen
    
    # print(targetNumberLen)

    numOfBitMasks = 2**(targetNumberLen)
    cntr = 0

    for bitMask in range(0, numOfBitMasks):
        # print("bitmask:", bitMask)
        numOfOnesInBitMask = numberOf1bits(bitMask)

        # print(numOfOnesInBitMask)

        if firstNumLen != numOfOnesInBitMask:
            continue
        else:
            possibleNumber = 0
            power = 1
            firstNumberCp = firstNumber
            secondNumberCp = secondNumber

            for _ in range(targetNumberLen):
                if bitMask % 2 == 1:
                    possibleNumber += power * (firstNumberCp % 10)
                    firstNumberCp = firstNumberCp // 10
                else: 
                    possibleNumber += power * (secondNumberCp % 10)
                    secondNumberCp = secondNumberCp // 10
                #end if
                power *= 10
                bitMask = bitMask // 2
            #end for
            
            print("possibleNumber", possibleNumber)

            if isPrime(possibleNumber):
                print("possibleNumber is prime")
                cntr += 1
        #end if
    #end for
    return cntr

if __name__ == "__main__":
    assert(numberOf1bits(5) == 2)
    isNumPrime = False
    for i in [2,3,5,11,23,41]:
        isNumPrime = isPrime(i)
        # print(isNumPrime)
        assert( isNumPrime== True)
    for j in [0,1,4,6,22]:
        isNumPrime = isPrime(j)
        # print(isNumPrime)
        assert(isNumPrime == False)


    firstNumber = int(input("enter first number: "))
    secondNumber = int(input("enter second number: "))
    
    print(solution(firstNumber, secondNumber))