from math import isqrt

def isPrime(num):
    if num == 2 or num ==3 :
        return True
    if num < 2 or num % 2 == 0 or num % 3 == 0:
        return False
    div = 5
    iroot = isqrt(num)
    while div < iroot:
        if num % div == 0:
            return False
        
        div += 2
        if num % div == 0:
            return False
        div += 4
    #end while
    return True


def print_2digital_primes(num, power=1, removed = 0, result = 0):

    if num == 0:
        if 10 <= result < 100 and removed > 0 and isPrime(result):
            print(result)
        #end if
        return
    #end if
    print_2digital_primes(num//10, power, removed + 1, result)
    lastDigit = num % 10
    print_2digital_primes(num//10, power * 10, removed, result + lastDigit * power)

if __name__ == "__main__":
    print_2digital_primes(42391)