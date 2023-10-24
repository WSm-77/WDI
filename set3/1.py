def changeBase(number):
    convertedNumber = ""
    while 0 != number:
        lastDigit = number % base
        if lastDigit > 9:
            lastDigit -= 10
            convertedNumber = chr(ord("A") + lastDigit) + convertedNumber
        else:
            convertedNumber = str(lastDigit) + convertedNumber
        #end if
        number //= base
    #end while
    return convertedNumber

if __name__ == "__main__":
    number = int(input("enter number: "))
    for base in range(2, 16 + 1):
        print("\nbase:", base)
        print(changeBase(number))