def isLastDigitUniqe(number):
    isUniqe = True
    lastDigit = number % 10

    while 0 != number:
        number = number // 10
        if number % 10 == lastDigit:
            isUniqe = False
            break
        #end if
    #end while

    return isUniqe

if __name__ == "__main__":
    number = int(input("enter number: "))
    print(isLastDigitUniqe(number))
