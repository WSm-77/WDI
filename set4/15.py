def doesContainPrimeDigit(number):
    result = False
    while 0 != number:
        if number % 10 in [2,3,5,7]:
            result = True
            break
        #end if
        number //= 10
    #end while
    return result

def solution(tab):
    tabLen = len(tab)
    result = False
    for R in range(tabLen):
        containsPrimeDigit = True
        for C in range(tabLen):
            if not doesContainPrimeDigit(tab[R][C]):
                containsPrimeDigit = False
                break
            #end if
        #end for
        if containsPrimeDigit:
            result = True
            break
        #end if
    #end for
    return result
            
if __name__ == "__main__":
    tab = [[2,0,0,0,0],
           [53,22,2,57,29],
           [0,2,0,0,0],
           [0,2,0,2,0],
           [0,0,2,2,0]]
    
    print(solution(tab))

    tab = [[41,441,114,668,88],
           [11,11,11,11,11],
           [43,6,89,5,3],
           [46,2,89,2,0],
           [43,0,39,3,5]]
    
    print(solution(tab))