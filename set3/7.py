from random import randint

def doesExsitElementWithOnlyOddDigits(numArray):
    doesExist = False
    for number in numArray:
        while 0 != number:
            currentDigit = number % 10
            if currentDigit % 2 == 0:
                break
            else:
                number //= 10
            #end if
        else:
            doesExist = True
            break
        #end while
    #end for
    return doesExist

if __name__ == "__main__":
    arrayLen = int(input("enter array length: "))
    numArray = [randint(1, 1000) for _ in range(arrayLen)]
    print(numArray)
    print(doesExsitElementWithOnlyOddDigits(numArray))