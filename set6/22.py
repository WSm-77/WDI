from math import isqrt

def jumps(T, index=0, numberOfJumps=0):
    N = len(T)
    if index == N - 1:
        return numberOfJumps
    if index >= N:
        return -1
    
    currentNum = T[index]
    div = 2
    iroot = isqrt(currentNum)
    while div <= iroot + 1 and div != T[index]:
        if currentNum % div == 0:
            result = jumps(T, index + div, numberOfJumps + 1)
            if result > -1:
                return result
            #end if
            while currentNum % div == 0:
                currentNum //= div
            #end while
        #end if
        div += 1
    #end while

    return -1

if __name__ == "__main__":
    tab = [6,1,1,4,5,9,1,1,7]

    print(jumps(tab))