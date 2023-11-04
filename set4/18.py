def maxSumInTable(tab):
    tabLen = len(tab)
    maxSum = 0
    for R in range(tabLen):
        for C in range(tabLen):
            #sum for row
            subArrayLen = 0
            currentSum = 0
            while subArrayLen < 10 and C + subArrayLen < tabLen:
                currentSum += tab[R][C + subArrayLen]
                maxSum = max(maxSum, currentSum)
                subArrayLen += 1
            #end while

            #sum for collumn
            subArrayLen = 0
            currentSum = 0
            while subArrayLen < 10 and R + subArrayLen < tabLen:
                currentSum += tab[R + subArrayLen][C]
                maxSum = max(maxSum, currentSum)
                subArrayLen += 1
            #end while
        #end for
    #end for
    return maxSum


if __name__ == "__main__":
    tab = [[1,0,3,4,5],
           [1,4,27,0,5],
           [1,1,42,9,7],
           [0,5,2,4,3],
           [1,1,1,1,0]]
    
    print("max sum:", maxSumInTable(tab))

    tab = [[-1,0,3,-4,5],
           [1,-4,27,0,5],
           [1,1,-42,-9,7],
           [0,-5,2,-4,3],
           [1,1,-1,60,0]]
    
    print("max sum:", maxSumInTable(tab))