from math import isqrt

def differentDigital(num):
    if num > 999999999:
        return False
    #end if
    digs = [0 for _ in range(10)]
    while num > 0:
        digs[num % 10] += 1
        num //= 10
    #end while
    return max(digs) == 1

def isPrime(num):
    if num == 2:
        return True
    elif num % 2 == 0 or num == 1 or num == 0:
        return False
    #end if
    div = 3
    iroot = isqrt(num)
    while div <= iroot:
        if num % div == 0:
            return False
        #end if
        div += 2
    #end while
    return True

def numberLen(num):
    if number == 0:
        return 1
    #end if
    result = 0
    while num > 0:
        result += 1
        num //= 10
    #end whlie
    return result


def main1(num):
    numLen = numberLen(num)
    maxDiffPrime = 0
    for _ in range(numLen):
        for M in range(numLen):
            for K in range(numLen - M):
                currentNumber = num // (10 ** K)
                currentNumber %= 10 ** (numLen - M - K)
                if differentDigital(currentNumber) and isPrime(currentNumber):
                    maxDiffPrime = max(maxDiffPrime, currentNumber)
                #end if
            #end for
        #end for
        lastDigit = num % 10
        num = num // 10 + (10 ** (numLen - 1)) * lastDigit
    #end for
    return maxDiffPrime

if __name__ == "__main__":
    number = 1202742516

    print(main1(number))