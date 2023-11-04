def pairsKnightMove(tab, targetProduct):
    tabLen = len(tab)
    moves = [(2,-1), (2,1), (1,2), (-1,2)]
    pairs = 0
    for R in range(tabLen):
        for C in range(tabLen):
            for move in moves:
                if 0 <= R + move[0] < tabLen and 0 <= C + move[1] < tabLen:
                    if tab[R][C] * tab[R + move[0]][C + move[1]] == targetProduct:
                        pairs += 1
                        # print(f"({R},{C}), ({R + move[0]},{C + move[1]})")
                    #end if
                #end if
            #end for
        #end for
    #end for
    return pairs

if __name__ == "__main__":
    tab = [[2,0,0,0,0],
           [0,0,2,0,0],
           [0,2,0,0,0],
           [0,2,0,2,0],
           [0,0,2,2,0]]
    
    print(pairsKnightMove(tab, 4))