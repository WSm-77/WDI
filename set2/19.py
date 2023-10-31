def numOf2and5(number):
    max2 = 0
    while number % 2 == 0:
        max2 += 1
        number //= 2
    #end while
    max5 = 0
    while number % 5 == 0:
        max5 += 1
        number //= 5
    #end while
    return max(max2, max5)

def periodicalFraction(numerator, denominator):
    print(numerator // denominator, end="")
    numerator %= denominator
    if numerator == 0:
        return
    #end if
    print(".", end="")
    beforePeriod = numOf2and5(denominator)
    for _ in range(beforePeriod):
        numerator *= 10
        print(numerator // denominator, end="")
        numerator %= denominator
    #end for
    if 0 == numerator:
        return
    print("(", end="")
    #end if
    rest = numerator
    while True:
        numerator *= 10
        print(numerator // denominator, end="")
        numerator %= denominator
        if rest == numerator:
            break
        #end if
    #end while
    print(")")

if __name__ == "__main__":
    numerator = 5
    denominator = 164
    periodicalFraction(numerator, denominator)