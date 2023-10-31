def doesContainEvenDig(number):
    doesContain = False
    while 0 != number:
        lastDigit = number % 10
        if lastDigit % 2 == 0:
            doesContain = True
            break
        #end if
        number //= 10
    #end while
    return doesContain

def doesExistRow(tab):
    tabLen = len(tab)
    doesExist = False
    for row in range(tabLen):
        doesExist = True
        for collumn in range(tabLen):
            if not doesContainEvenDig(tab[row][collumn]):
                doesExist = False
                break
            #end if
        #end for
        if doesExist:
            break
        #end if
    #end for
    return doesExist

if __name__ == "__main__":
    tab = [[12,13,4],
           [3,42,2],
           [24,135,8]]
    print(doesExistRow(tab))

    tab = [[12,13,4],
           [24,125,8],
           [3,42,2]]
    print(doesExistRow(tab))

    tab = [[12,13,4,2],
           [24,57,12,4],
           [3,42,2,2],
           [24,135,8,2]]
    print(doesExistRow(tab))

    tab = [[12,13,4,2],
           [24,27,12,4],
           [3,42,2,2],
           [24,135,8,2]]
    print(doesExistRow(tab))