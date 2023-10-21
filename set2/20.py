def isVariousDigital(firstNum, secondNum, base):
    variousDigital = True
    
    while 0 != firstNum:
        lastDigit = firstNum % base
        secondNumCopy = secondNum

        while 0 != secondNumCopy:
            if lastDigit == secondNumCopy % base:
                variousDigital = False
                break
            #end if
            secondNumCopy = secondNumCopy // base
        #end while

        if not variousDigital:
            break
        #end if

        firstNum = firstNum // base
    #end while

    return variousDigital

# this is used only to visualise numbers in systems with different bases
# it is not part of the solution 

def convertBase(firstNum, secondNum, base):
    power = 1
    convertedFirst = convertedSecond = 0

    while 0 != firstNum or 0 != secondNum:
        convertedFirst += (firstNum % base) * power
        convertedSecond += ( secondNum% base) * power
        firstNum = firstNum // base
        secondNum = secondNum // base
        power *= 10
    #end while

    print("converted first:", convertedFirst)
    print("converted second:", convertedSecond)

if __name__ == "__main__":
    firstNum = int(input("enter first number: "))
    secondNum = int(input("enter second number: "))
    for base in range(2, 16 + 1):
        print()
        print("base:", base)
        convertBase(firstNum, secondNum, base)
        myVariousDigital = isVariousDigital(firstNum, secondNum, base)
        if myVariousDigital:
            print("this numbers are various digital")
            break
        else:
            print("this numbers are NOT various digital")
    #end for

    ###################
    # actula solution #
    ###################
    print()
    if myVariousDigital:
        print(base)
    else:
        print("such base does not exist")