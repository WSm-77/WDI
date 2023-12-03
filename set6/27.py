def dont_intersect(sqr1, sqr2):
    return sqr2[0] > sqr1[1] or sqr2[1] < sqr1[0] or sqr2[2] > sqr1[3] or sqr1[3] < sqr1[2]

def choose_squares(T):
    usedSquares = []
    def rek(T, usedSquares, index = 0, currentSum = 2012):
        if currentSum < 0:
            return False
        if index == len(T):
            # return True if currentSum == 0 and len(usedSquares) == 13 else False
            return True if currentSum == 0 and len(usedSquares) == 6 else False
        
        if rek(T, usedSquares, index + 1, currentSum):
            return True
        
        flag = True
        for square in usedSquares:
            if not dont_intersect(square, T[index]):
                flag = False
                break
            #end if
        #end for
        if flag:
            usedSquares.append(T[index])
            result = rek(T, usedSquares, index + 1, currentSum - ((T[index][1] - T[index][0])**2))
            usedSquares.pop()
            if result:
                return True
            #end if
        #end if
        return False
    #end def
    return rek(T, usedSquares)

if __name__ == "__main__":
    tab = [(0,1,0,1), (2,5,2,5), (6,50,6,50), (51,59,51,59), (60,61,60,61), (62,63,62,63)]
    print(choose_squares(tab))

    # print("do intersect:", not dont_intersect((4,6,4,6), (3,5,3,5)))
    
    tab = [(0,1,0,1), (2,5,2,5), (6,50,6,50), (51,59,51,59), (60,61,60,61), (62,64,62,64)]
    print(choose_squares(tab))