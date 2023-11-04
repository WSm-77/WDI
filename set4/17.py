def solution(tab):
    tabLen = len(tab)
    maxSum = tab[0][1] + tab[1][0] + tab[0][0]
    neighbours = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    maxElemRow = 0
    maxElemColl = 0
    for R in range(tabLen):
        for C in range(tabLen):
            currentSum = 0
            for neighbour in neighbours:
                if 0 <= R + neighbour[0] < tabLen and 0 <= C + neighbour[1] < tabLen:
                    currentSum += tab[R + neighbour[0]][C + neighbour[1]]
                    if currentSum > maxSum:
                        maxSum = currentSum
                        maxElemRow = R
                        maxElemColl = C
                    #end if
                #end if
            #end for
        #end for
    #end for
    return (maxElemRow, maxElemColl)

if __name__ == "__main__":
    tab = [[235,1,1,1,1],
           [1,1,35,1,1],
           [1,727,1,1,1],
           [1,1,1,732,1],
           [1,523,1,1,1]]

    print(solution(tab))

    tab = [[4,-10,2],
           [10,5,-2],
           [-20,20,23]]
    
    print(solution(tab))