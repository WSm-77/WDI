PRECISION = 6

def printDecimalExpansion(numerator, denominator):
    #reszta z dzielenia  
    remainder = numerator % denominator
    print(numerator//denominator, end=".")
    for _ in range(PRECISION):
        remainder *= 10
        print(remainder // denominator, end="")
        remainder %= denominator
    #end for
    print()



if __name__ == "__main__":
    numerator = int(input("enter numerator: "))
    denominator = int(input("enter denominator: "))
    printDecimalExpansion(numerator, denominator)
    