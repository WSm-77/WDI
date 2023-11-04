def rowSum(tab, R):
    tabLen = len(tab)
    sum = 0
    for C in range(tabLen):
        sum += tab[R][C]
    #end for
    return sum

def collSum(tab, C):
    tabLen = len(tab)
    sum = 0
    for R in range(tabLen):
        sum += tab[R][C]
    #end for
    return sum

def solution(tab):
    tabLen = len(tab)
    firstRookRowIndex = firstRookCollIndex = secondRookRowIndex = 0
    secondRookCollIndex = 1
    maxSum = rowSum(tab, 0) + collSum(tab, 0) + collSum(tab, 1) - 2 * tab[0][0] - 2 * tab[0][1]     # allternatively: maxSum = -float('inf')
    for R1 in range(tabLen - 1):
        for C1 in range(tabLen - 1):
            for R2 in range(R1, tabLen):
                for C2 in range(C1, tabLen):
                    if R1 == R2 and C1 == C2:
                        continue
                    #end if
                    currentSum = rowSum(tab, R1) + collSum(tab, C1) - 2 * tab[R1][C1]
                    if R1 == R2:
                        currentSum += collSum(tab, C2) - 2 * tab[R2][C2]
                    elif C1 == C2:
                        currentSum += rowSum(tab, R2) - 2 * tab[R2][C2]
                    else:
                        currentSum += rowSum(tab, R2) + collSum(tab, C2) - (2 * tab[R2][C2] + tab[R1][C2] + tab[R2][C1])
                    #end if
                    if currentSum > maxSum:
                        maxSum = currentSum
                        firstRookRowIndex, firstRookCollIndex, secondRookRowIndex, secondRookCollIndex = R1, C1, R2, C2
                #end for
            #end for
        #end for
    #end for
    return ((firstRookRowIndex, firstRookCollIndex), (secondRookRowIndex, secondRookCollIndex))

if __name__ == "__main__":
    tab = [[1,0,3,4,5],
           [1,4,27,0,5],
           [1,1,42,9,7],
           [0,5,2,4,3],
           [1,1,1,1,0]]

    print(solution(tab))

    tab = [[2,0,0,0,0],
           [0,0,2,0,0],
           [0,2,0,0,0],
           [0,2,0,2,0],
           [0,0,2,2,0]]
    
    print(solution(tab))
    
    tab = [[0,1000,1000,1000],
           [1000,0,0,0],
           [0,1000,1000,1000],
           [1000,0,0,0]]
    
    print(solution(tab))

    tab =   [[1, 2, 3, 4, 5, 6, 7],
            [24, 25, 26, 27, 28, 29, 8],
            [23, 40, 41, 42, 43, 30, 9],
            [22, 39, 48, 49, 44, 31, 10],
            [21, 38, 47, 46, 45, 32, 11],
            [20, 37, 36, 35, 34, 33, 12],
            [19, 18, 17, 16, 15, 14, 13]]
    
    print(solution(tab))