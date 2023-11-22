from random import randint

def solution(T, Row, Coll):
    moves = [(1, 0), (0, 1), (1, 1)]

    def numberLen(num):
        numLen = 0
        while num > 0:
            numLen += 1
            num //= 10
        #end while
        return numLen
    #end def

    def isLegalMove(T, C, R, lastDigit):
        N = len(T)
        if 0 <= C < N and 0 <= R < N:
            firstDigit = T[R][C]
            numLen = numberLen(firstDigit)
            firstDigit = firstDigit // (10 ** (numLen - 1))
            return True if lastDigit < firstDigit else False
        else:
            return False
        
    def rek(T, R, C):
        if R == C == len(T) - 1:
            return True
        #end if
        isPossible = False
        for nextR, nextC in moves:
            if isLegalMove(T, R + nextR, C + nextC, T[R][C] % 10):
                isPossible = isPossible or rek(T, R + nextR, C + nextC)
            #end if
        #end for
        return isPossible
    #end def

    return rek(T, Row, Coll)

if __name__ == "__main__":
    # tab = [ [randint(1,15) for _ in range(8)] for _ in range(8) ]
    tab = [[15, 6, 1, 5, 13, 2, 13, 12],
            [7, 14, 9, 6, 8, 12, 8, 2],
            [10, 6, 10, 4, 13, 10, 13, 6],
            [1, 10, 12, 15, 7, 6, 13, 8],
            [10, 10, 8, 5, 4, 6, 9, 4],
            [12, 11, 6, 11, 5, 10, 2, 7],
            [1, 8, 7, 10, 7, 14, 14, 3],
            [15, 14, 14, 14, 3, 15, 53, 45]]
    
    print(*tab, sep='\n')

    print(solution(tab, 6, 6))