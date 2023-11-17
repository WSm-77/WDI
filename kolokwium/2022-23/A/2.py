def isInSeq(num):
    a, b = 1, 2
    while a < num:
        a, b = b, a + b - 1
    #end while
    return a == num

def seq(T):
    N = len(T)
    for R in range(N - 2):
        for C in range(N - 2):
            if T[R][C] + T[R + 1][C + 1] - 1 == T[R + 2][C + 2]:
                if isInSeq(T[R][C]):
                    seqLen = 3
                    i = 1
                    while R + i + 2 < N and C + i + 2 < N:
                        if T[R + i][C + i] + T[R + i + 1][C + i + 1] - 1 == T[R + i + 2][C + i + 2]:
                            seqLen += 1
                            i += 1
                        else:
                            break
                        #end if
                    #end while
                    return seqLen
                #end if
            #end if
        #end for
    #end for
    return 0

if __name__ == "__main__":
    tab = [[4,1,3,4,6],
           [1,2,2,3,4],
           [1,5,3,2,5],
           [4,1,3,9,3],
           [7,7,7,7,7]]
    
    print(seq(tab))