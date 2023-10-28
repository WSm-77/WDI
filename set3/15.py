from math import isqrt

def isPrime(number):
    if number == 2:
        return True
    elif number < 2 or number % 2 == 0:
        return False
    else:
        div = 3
        iroot = isqrt(number)
        while div <= iroot:
            if number % div == 0:
                return False
            else:
                div += 2
            #end if
        #end while
        return True
    #end if

def solution(numArray):
    result = False
    n = len(numArray)
    fib1, fib2 = 1, 2
    for i in range(n):
        currentNumber = numArray[i]
        if i == fib1:
            if isPrime(currentNumber) or currentNumber < 2:
                result = False
                break
            #end if

            fib1, fib2 = fib2, fib1 + fib2
        #end if
        else:
            if isPrime(currentNumber):
                result = True
            #end if
        #end if
    #end for
    return result

if __name__ == "__main__":
    numArray = [0,4,6,18,7,1]
    print(solution(numArray))
    numArray = [0,4,6,18,7,12]
    print(solution(numArray))