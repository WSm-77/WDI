def onlyOddDigits(number):
    result = True
    while 0 != number:
        lastDigit = number % 10
        if lastDigit % 2 == 0:
            result = False
            break
        #end if
        number //= 10
    #end while
    return result

def existsOnlyOddInEveryRow(tab):
    tabLen = len(tab)
    doesExist = True
    for row in range(tabLen):
        for collumn in range(tabLen):
            doesExist = onlyOddDigits(tab[row][collumn])
            if doesExist:
                break
            #end if
        #end for
        if not doesExist:
            break
    #end for
    return doesExist

if __name__ == "__main__":
    tab = [[12,13,4],
           [3,42,2],
           [24,135,8]]
    print(existsOnlyOddInEveryRow(tab))

    tab = [[12,4,4],
           [3,42,2],
           [24,135,8]]
    print(existsOnlyOddInEveryRow(tab))

    tab = [[12,13,4,2],
           [24,57,12,4],
           [3,42,2,2],
           [24,135,8,2]]
    print(existsOnlyOddInEveryRow(tab))
