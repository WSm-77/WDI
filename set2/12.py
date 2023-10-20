def numOfDigits(number):
    digits = 0
    while 0 != number:
        digits += 1
        number = number // 10
    #end while
    return digits

def doesContainNumberOfDigits(number):
    myDigitsNum = numOfDigits(number)
    
    result = False

    if myDigitsNum <= 9:
        while 0 != number:
            if myDigitsNum == number % 10:
                result = True
                break
            #end if
            number = number // 10
        #end while
    #end if

    return result

def doesContainNumberOfDigitsUpgraded(number):
    myDigitsNum = numOfDigits(number)
    
    result = False

    power = 10 ** numOfDigits(myDigitsNum)

    while 0 != number:
        if myDigitsNum == number % power:
            result = True
            break
        #end if
        number = number // 10
    #end while


    return result


if __name__ == "__main__":
    number = int(input("enter number: "))
    print("does number contain digit that represents number of it's digits:", doesContainNumberOfDigits(number))
    print("does number contain number that represents number of it's digits:", doesContainNumberOfDigitsUpgraded(number))