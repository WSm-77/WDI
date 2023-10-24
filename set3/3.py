from math import isqrt

def erastotnesSieve(maxNumber):
    isPrime = [True for _ in range(maxNumber + 1)]
    isPrime[0] = isPrime[1] = False
    iroot = isqrt(maxNumber)
    for prime in range(iroot + 1):
        if not isPrime[prime]:
            continue
        #end if
        for j in range(prime*prime, maxNumber + 1, prime):
            isPrime[j] = False
        #end for
    #end for
    return [i for i in range(maxNumber + 1) if isPrime[i]]


if __name__ == "__main__":
    maxNumber = int(input("enter number: "))
    print(*erastotnesSieve(maxNumber), sep="\n")