from math import sqrt

def main():
    sumOfDigits = 101
    buildNumber(sumOfDigits, 1, getNumberLength(sumOfDigits))

def getNumberLength(number):
    numberLength = 0

    if 0 == number:
        return 1
    
    while 0 != number:
        number = number // 10
        numberLength += 1

    return numberLength

def buildNumberFromList(listOfDigits):
    number = 0
    currentPower = 1
    for i in listOfDigits:
        number += i*(10**currentPower)
        currentPower += 1


# this function builds number with sum of digits that equals "targetSum"
def buildNumber(targetSum, currentPower, remainingNumberLength):
    buildFirstDigits(targetSum, currentPower, remainingNumberLength)

def buildFirstDigits(targetSum, currentPower, remainingNumberLength):
    firstDigits = 1
    buildRemaining(targetSum - firstDigits, currentPower - 1, firstDigits, remainingNumberLength - 1, [])


def buildRemaining(targetSum, currentPower, firstDigits, remainingNumberLength, usedDigits):
    if 0 == remainingNumberLength:
        return buildNumberFromList(usedDigits)



    
    


    



main()