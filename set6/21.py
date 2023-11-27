def does_sum_exist(T, targetSum):
    N = len(T)
    usedColls = [False for _ in range(N)]

    def rek(T, targetSum, usedNums, R=0, currentSum=0):
        nonlocal N
        if currentSum == targetSum:
                print(usedNums)
                return True
        #end if
        if currentSum > targetSum or R == N:
            return False
        #end if
        for C in range(N):
            if usedColls[C]:
                continue
            #end if
            result = rek(T, targetSum, usedNums, R + 1, currentSum)
            if result:
                return True
            #end if
            usedColls[C] = True
            result = rek(T, targetSum, usedNums + [T[R][C]], R + 1, currentSum + T[R][C])
            usedColls[C] = False
            if result:
                return True
            #end if
        #end for

        return False
    #end def
    return rek(T, targetSum, [])

if __name__ == "__main__":
    tab = [[15, 6, 1, 5, 13, 2, 13, 12],
           [7, 14, 9, 6, 8, 12, 8, 2],
           [10, 6, 10, 4, 13, 10, 13, 6],
           [1, 10, 12, 15, 7, 6, 13, 8],
           [10, 10, 8, 5, 1, 6, 9, 4],
           [12, 11, 6, 41, 5, 10, 2, 7],
           [1, 8, 7, 40, 7, 14, 14, 3],
           [95, 14, 14, 14, 3, 15, 53, 45]]
    
    print(does_sum_exist(tab, 79))

    tab = [[15, 6, 1, 5, 13, 2, 13, 12],
           [7, 14, 9, 6, 8, 12, 8, 2],
           [10, 6, 10, 4, 13, 10, 13, 6],
           [1, 10, 12, 15, 7, 6, 13, 8],
           [10, 10, 8, 5, 1, 6, 9, 4],
           [12, 11, 6, 41, 5, 10, 2, 7],
           [1, 8, 7, 40, 7, 14, 14, 3],
           [95, 14, 14, 14, 3, 15, 53, 45]]
    
    print(does_sum_exist(tab, 7000))

    # tab = [[1, 2, 3, 4, 5, 6, 7, 8],
    #       [28, 29, 30, 31, 32, 33, 34, 9],
    #       [27, 48, 49, 50, 51, 52, 35, 10],
    #       [26, 47, 60, 61, 62, 53, 36, 11],
    #       [25, 46, 59, 64, 63, 54, 37, 12],
    #       [24, 45, 58, 57, 56, 55, 38, 13],
    #       [23, 44, 43, 42, 41, 40, 39, 14],
    #       [22, 21, 20, 19, 18, 17, 16, 15]]
    
    # print(does_sum_exist(tab, 162))