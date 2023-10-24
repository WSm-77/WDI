from math import isqrt
from random import randint

def primeDivisors(number):
    dividers = set()
    div = 2
    iroot = isqrt(number)
    while div <= iroot:
        while number % div == 0:
            dividers.add(div)
            number //= div
        #end while

        div += 1
        iroot = isqrt(number)
    #end while
    if 1 != number:
        dividers.add(number)
    #end if
    return dividers


    return dividers

def isLastElementAchiveable(tab):
    tabLen = len(tab)
    isAchiveable = [False for _ in range(tabLen)]
    isAchiveable[0] = True
    for i in range(tabLen):
        if not isAchiveable[i]:
            continue
        #end if
        dividers = primeDivisors(tab[i])
        for div in dividers:
            if  i + div >= tabLen:
                break
            #end if
            isAchiveable[i + div] = True
        #end for
    #end for
    print(isAchiveable)
    return isAchiveable[tabLen - 1]


if __name__ == "__main__":
    assert(isLastElementAchiveable([6,2,2,3,5,6,7,11,19,3]))
    assert(primeDivisors(732) == {2,3,61})
    numberOfElements = int(input("enter number of elements in tab: "))
    tab = [randint(1, 100) for _ in range(numberOfElements)]
    print(tab)
    print(isLastElementAchiveable(tab))