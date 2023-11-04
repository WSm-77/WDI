def onlyPrimeDigits(number):
    result = True
    while 0 != number:
        if not number % 10 in [2,3,5,7]:
            result = False
            break
        #end if
        number //= 10
    #end while
    return result

def solution(tab):
    tabLen = len(tab)
    result = True
    for R in range(tabLen):
        oneWithOnlyPrimeDigits = False
        for C in range(tabLen):
            if onlyPrimeDigits(tab[R][C]):
                oneWithOnlyPrimeDigits = True
                break
            #end if
        #end for
        if not oneWithOnlyPrimeDigits:
            result = False
            break
        #end if
    #end for
    return result

if __name__ == "__main__":
    tab = [[235,1,1,1,1],
           [1,1,35,1,1],
           [1,727,1,1,1],
           [1,1,1,732,1],
           [1,523,1,1,1]]

    print(solution(tab))
    
    tab = [[235,1,1,1,1],
           [1,1,35,1,1],
           [1,727,1,1,1],
           [1,1,1,7432,1],
           [1,523,1,1,1]]

    print(solution(tab))