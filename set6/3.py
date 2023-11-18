##################################
# first solution (with nonlocal )#
##################################

def minimal_cost_to_reach_7th_row(T, C):
    minCost = float('inf')

    def move_king(C, R, currentCost):
        if not 0<= C < 8:
            return
        if R == 7:
            nonlocal minCost
            minCost = min(minCost, currentCost + T[R][C])
            return
        
        move_king(C - 1, R + 1, currentCost + T[R][C])
        move_king(C, R + 1, currentCost + T[R][C])
        move_king(C + 1, R + 1, currentCost + T[R][C])
    #end def
    move_king(C, 0, 0)
    return minCost

######################################
# second solution (without nonlocal) #
######################################

def min_cost(T, C, R=0, cost=0):
    if R == 7:
        return T[R][C]
    left = right = float('inf')
    if C > 0:
        left = min_cost(T, C - 1, R + 1, cost)
    if C < 7:
        right = min_cost(T, C + 1, R + 1, cost)
    
    middle = min_cost(T, C, R + 1, cost)
    return min(left, middle, right) + T[R][C]

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
        print("first solution (nonlocal):", minimal_cost_to_reach_7th_row(T, i))
        print("second solution (without nonlocal):", min_cost(T, i))
