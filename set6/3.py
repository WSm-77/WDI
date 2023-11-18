def minimal_cost_to_reach_7th_row(T, C):
    minCost = float('inf')

    def move_king(T, C, R, currentCost):
        if not 0<= C < 8:
            return
        if R == 6:
            nonlocal minCost
            minCost = min(minCost, currentCost)
            return
        
        move_king(T, C - 1, R + 1, currentCost + T[R][C])
        move_king(T, C, R + 1, currentCost + T[R][C])
        move_king(T, C + 1, R + 1, currentCost + T[R][C])
    #end def
    move_king(T, C, 0, 0)
    return minCost

if __name__ == "__main__":
    T = [[15, 17, 11, 15, 15, 19, 6, 9],
        [20, 5, 18, 8, 15, 4, 4, 4],
        [1, 14, 20, 16, 17, 17, 15, 17],
        [14, 2, 2, 10, 20, 16, 15, 13],
        [12, 18, 18, 12, 7, 4, 18, 1],
        [19, 20, 18, 13, 16, 9, 2, 8],
        [4, 9, 5, 6, 5, 5, 10, 4],
        [2, 9, 10, 19, 19, 7, 8, 15]]
    
    for i in range(8):
        print(minimal_cost_to_reach_7th_row(T, i))
