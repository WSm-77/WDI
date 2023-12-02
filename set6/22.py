from math import isqrt

def isPrime(num):
    if num == 2 or num == 3:
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

def exclusive_min(res, jump):
    if res == -1:
        return jump
    elif jump < res:
        return jump
    else:
        return res

def jumps(T, index=0, numberOfJumps=0):
    N = len(T)
    if index == N - 1:
        return numberOfJumps
    if index >= N:
        return -1
    
    currentNum = T[index]
    div = 2
    result = -1
    while div <= isqrt(currentNum):
        if currentNum % div == 0:
            result = exclusive_min(result, jumps(T, index + div, numberOfJumps + 1))
            while currentNum % div == 0:
                currentNum //= div
            #end while
        #end if
        div += 1
    else:
        if isPrime(currentNum) and currentNum != T[index]:
            result = exclusive_min(result, jumps(T, index + currentNum, numberOfJumps + 1))
    #end while

    return result

if __name__ == "__main__":
    tab = [6,1,1,4,5,9,1,1,7]

    print(jumps(tab))

    tab = [6,1,1,4,5,2,1,1,7]

    print(jumps(tab))

    tab = [30,1,6,4,5,9,1,1,7]

    print(jumps(tab))