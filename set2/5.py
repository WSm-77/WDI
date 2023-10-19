def calculateNumberLen(number):
    len = 0
    while 0 != number:
        len += 1
        number = number // 10
    #end while
    return len

def solution(number, div):
    cntr = 0
    numberLen = calculateNumberLen(number)
    numOfBitMasks = 2 ** (numberLen)

    for bitMask in range(1, numOfBitMasks):
        possibleNumber = 0
        power = 1
        numberCp = number

        for _ in range(numberLen):
            if bitMask % 2 == 1:
                possibleNumber += power * (numberCp % 10)
                power *= 10
            #endif
            numberCp = numberCp // 10
            bitMask = bitMask // 2
        #end for

        print("possibleNumber:", possibleNumber)

        if possibleNumber % div == 0:
            print("is divideable")
            cntr += 1
        #end if
    #end for
    return cntr

if __name__ == "__main__":
    assert(calculateNumberLen(123) == 3)
    assert(calculateNumberLen(1234) == 4)
    assert(solution(7,7) == 1)
    assert(solution(2315,7) == 4)

    number = int(input("enter number: "))
    div = int(input("enter divisor: "))
    print(solution(number, div))
#end if