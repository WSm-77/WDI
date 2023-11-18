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

def cut(T, currentNum=0, index=0, currentLen=0):
    if index == len(T):
        return isPrime(currentNum)
    elif currentLen > 30:
        return False
    #end if

    currentNum = 2*currentNum + T[index]
    case1 = case2 = False
    index += 1
    if isPrime(currentNum):
        case1 = cut(T, 0, index, 0) or cut(T, currentNum, index, currentLen + 1)
    else:
        case2 = cut(T, currentNum, index, currentLen + 1)
    #end if
    
    return case1 or case2

if __name__ == "__main__":
    tab = [1,1,1,0,1,1]
    print(cut(tab))
    
    tab = [1,1,0,1,0,0]
    print(cut(tab))