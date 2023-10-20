def areDigitsInIncreasingOrder(number):
    result = True
    previousDigit = 10
    while 0 != number:
        lastDigit = number % 10
        if previousDigit <= lastDigit:
            result = False
            break
        previousDigit = lastDigit
        number = number // 10
    #end while
    return result

if __name__ == "__main__":
    number = int(input("enter number: "))
    if areDigitsInIncreasingOrder(number):
        print("yes")
    else:
        print("no")