def areSameDigital(firstNumber, secondNumber):
    firstNumber = str(firstNumber)
    secondNumber = str(secondNumber)
    if len(firstNumber) != len(secondNumber):
        return False
    else:
        return sorted(firstNumber) == sorted(secondNumber)

if __name__ == "__main__":
    firstNum = int(input("enter first number: "))
    secondNum = int(input("enter second number: "))
    if areSameDigital(firstNum, secondNum):
        print("this numbers are same digital")
    else:
        print("this numbers are NOT same digital")