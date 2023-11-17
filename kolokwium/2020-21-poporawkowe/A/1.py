def longestGeometric(T):
    N = len(T)
    maxLen = 0
    i = 0
    while T[i][0] == 0:
        i += 1
        maxLen += 1
    #end while
    prevNum = T[i][0] / T[i][1]
    i += 1
    if i >= N:
        return maxLen if maxLen > 2 else 0
    #end if
    prevq = (T[i][0] / T[i][1]) / (prevNum)
    prevNum = T[i][0] / T[i][1]
    currentLen = 2
    while i < N - 1:
        i += 1
        currentNum = T[i][0] / T[i][1]
        if prevNum == 0:
            if currentNum == 0:
                currentLen += 1
            else:
                currentLen = 2
            #end if
            prevq = 0
        else:
            currentq = currentNum / prevNum
            if currentq == prevq:
                currentLen += 1
                maxLen = max(maxLen, currentLen)
            else:
                currentLen = 2
                prevq = currentq
            #end if
        #end if
        prevNum = currentNum
    #end while
    return maxLen

if __name__ == "__main__":
    tab =  [(0,2),(1,2),(2,2),(4,2),(4,1),(5,1)]

    print(longestGeometric(tab))