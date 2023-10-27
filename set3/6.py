from random import randint

def doesContainOddDigit(numArray):
    doesContOddDig = True
    for number in numArray:
        while 0 != number:
            currentDigit = number % 10            
            if currentDigit % 2 == 1:
                break
            else:
                number //= 10
            #end if
        else:
            doesContOddDig = False
            break
        #end while
    #end for
    return doesContOddDig


if __name__ == "__main__":
    arrayLen = int(input("enter array length: "))
    numArray = [randint(1, 1000) for _ in range(arrayLen)]
    print(numArray)
    print(doesContainOddDigit(numArray))