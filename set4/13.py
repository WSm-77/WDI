from math import isqrt

def isPrime(num):
    prime = True
    div = 2
    iroot = isqrt(num)

    while div <= iroot:
        if num % div == 0:
            prime = False
            break
        #end if

        div += 1
    #end while

    return prime

def removeNotComplementaryNums(tab):
    tabLen = len(tab)
    for C1 in range(tabLen):
        for R1 in range(tabLen):
            hasComplementary = False

            for C2 in range(tabLen):
                for R2 in range(tabLen):
                    if (C1 == C2 and R1 == R2) or tab[R2][C2] == 0:
                        continue
                    #end if
                    if isPrime(tab[R1][C1] + tab[R2][C2]):
                        hasComplementary = True
                    #end if
                #end for

                if hasComplementary:
                    break
                #end if
            #end for

            if not hasComplementary:
                tab[R1][C1] = 0
            #end if
        #end for
    #end for

if __name__ == "__main__":
    tab = [[4,10,2],
           [10,5,2],
           [20,20,23]]
    
    removeNotComplementaryNums(tab)

    print(*tab, sep='\n', end='\n\n')

    tab = [[4,10,2],
           [10,5,2],
           [23,12,23]]
    
    removeNotComplementaryNums(tab)

    print(*tab, sep='\n')
