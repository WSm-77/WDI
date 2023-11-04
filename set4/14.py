def numberOfOnesInBinary(num):
    onesCntr = 0
    while 0 != num:
        onesCntr += num % 2
        num >>= 1       # equivalent of num //= 2
    #end while
    return onesCntr

def solution(tab1, tab2):
    tab1Len = len(tab1)
    tab2Len = len(tab2)

    for R1 in range(tab1Len - tab2Len + 1):
        for C1 in range(tab1Len - tab2Len + 1):

            compatibileCntr = 0

            for R2 in range(tab2Len):
                for C2 in range(tab2Len):
                    if numberOfOnesInBinary(tab1[R2 + R1][C2 + C1]) == numberOfOnesInBinary(tab2[R2][C2]):
                        compatibileCntr += 1
                    #end if
                #end for
            #end for

            if compatibileCntr / (tab1Len * tab1Len) > 0.33:

                return True
            
            #end if
        #end for
    #end for

    return False

if __name__ == "__main__":
    tab1 = [[0,0,0,0],
            [14,0,14,0],
            [14,14,14,0],
            [14,14,14,0]]
    
    tab2 = [[22,0,22],
            [22,0,22],
            [22,0,22]]
    
    print(solution(tab1,tab2))

    tab1 = [[0,4,0,4],
            [1,0,1,0],
            [1,1,1,4],
            [1,0,1,0]]
    
    tab2 = [[3,0,0],
            [0,3,0],
            [0,0,3]]
    
    print(solution(tab1,tab2))

    tab1 = [[0,4,0,4],
            [5,4,5,0],
            [5,5,5,4],
            [5,4,9,0]]
    
    tab2 = [[9,0,3],
            [9,3,0],
            [3,0,3]]
    
    print(solution(tab1,tab2))