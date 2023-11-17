def seq(T):
    n = len(T)
    maxLen = 0
    a1 = a2 = 0
    for R in range(n - 2):
        # ele = 0
        C = 0
        while C < n - 2:
            iterator = 1
            a1 = T[R][C]
            a2 = T[R][C + iterator]
            currentLen = 1
            while C + iterator < n and R + iterator < n:
                if T[R + iterator][C] == T[R][C + iterator] == a2:
                    currentLen += 1
                    maxLen = max(maxLen, currentLen)
                    iterator += 1
                    a1, a2 = a2, a1 + a2 - 1
                else:
                    break
                #end if
            #end while
            C += 1
        #end while
    #end for
    return maxLen

if __name__ == "__main__":
    tab =   [[8,1,2,1,2,1],
            [2,3,4,6,9,14],
            [4,4,5,6,7,8],
            [1,6,9,2,1,6],
            [3,9,6,1,4,1],
            [7,14,5,6,1,7]]
    
    print(seq(tab))

    tab =   [[1,2,2,3,4,6],
            [2,3,4,6,9,14],
            [2,4,5,6,7,8],
            [3,6,9,2,1,6],
            [4,9,6,1,4,1],
            [6,14,5,6,1,7]]
    
    print(seq(tab))

    tab =   [[1,2,2,5,4,6],
            [2,3,4,6,9,7],
            [2,4,1,4,4,7],
            [3,2,4,2,1,6],
            [4,9,4,1,4,1],
            [6,1,7,6,1,7]]
    
    print(seq(tab))