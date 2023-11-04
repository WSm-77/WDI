def areFriends(firstNum, secondNum):
    divs = [0 for _ in range(10)]
    while 0 != firstNum:
        divs[firstNum % 10] = 1
        firstNum //= 10
    #end while
    while 0 != secondNum:
        if divs[secondNum % 10] == 0:
            return False
        else:
            divs[secondNum % 10] = 2
        secondNum //= 10

    for div in divs:
        if div == 1:
            return False
    return True

def findAllNumbersSurroundedByFriends(tab):
    tabLen = len(tab)
    neighbours = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    allNumbers = 0
    for R in range(tabLen):
        for C in range(tabLen):
            currentNum = tab[R][C]
            everNeighbourIsfriend = True
            for neighbour in neighbours:
                if (0 <= R + neighbour[0] < tabLen) and (0 <= C + neighbour[1] < tabLen):
                    if not areFriends(tab[R + neighbour[0]][C + neighbour[1]], currentNum):
                        everNeighbourIsfriend = False
                        break
                    #end if
                #end if
            if everNeighbourIsfriend:
                allNumbers += 1
            #end for
        #end for
    #end for
    return allNumbers

if __name__ == "__main__":
    tab = [[223,23,223,0,1],
           [233,32,332,0,0],
           [0,2,0,0,0],
           [0,2,0,55,55],
           [1,0,2,55,5]]
    
    print(findAllNumbersSurroundedByFriends(tab))

    tab = [[223,23,223,323,2323],
           [233,32,332,32,23],
           [23,23,23,23,23],
           [3332,23233,232,55,55],
           [23323,23,2332,55,5]]
    
    print(findAllNumbersSurroundedByFriends(tab))