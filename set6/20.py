from random import randint

def solution(T, startRow, startColl):
    N = len(T)
    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def firstDigit(num):
        while num > 9:
            num //= 10
        #end while
        return num
    #end def

    def isMovePossible(T, lastDigit, nextRow, nextColl):
        N = len(T)
        if 0 <= nextRow < N and 0 <= nextColl < N:
            if lastDigit < firstDigit(T[nextRow][nextColl]):
                return True
            #end if
        #end if
        return False
    #end def
        
    def isCloserToTarget(prevPos, nextPos, targetCorner):
        return abs(nextPos[0] - targetCorner[0]) <= abs(prevPos[0] - targetCorner[0]) and abs(nextPos[1] - targetCorner[1])  <= abs(prevPos[1] - targetCorner[1])
    #end def

    def rek(T, R, C, targetCorner, currentPath):
        if (R, C) == targetCorner:
            nonlocal path
            path = currentPath
            return True
        
        result = False

        for move in moves:
            nextRow = R + move[0]
            nextColl = C + move[1]
            
            if isCloserToTarget((R, C), (nextRow, nextColl), targetCorner) and isMovePossible(T, T[R][C], nextRow, nextColl):
                # currentPath.append()
                result = result or rek(T, nextRow, nextColl, targetCorner, currentPath + [(nextRow, nextColl)])
                # currentPath.pop()
                if result:
                    break
                #end if
            #end if
        #end for

        return result
    #end def

    path = []

    result = False
    for corner in [(0, 0), (0, N - 1), (N - 1, 0), (N - 1, N - 1)]:
        result = result or rek(T, startRow, startColl, corner, [(startRow, startColl)])
        if result:
            break
        #end if
    #end for

    return result, path

if __name__ == "__main__":
    # tab = [ [randint(1,15) for _ in range(8)] for _ in range(8) ]

    tab = [[15, 6, 1, 5, 13, 2, 13, 12],
            [7, 14, 9, 6, 8, 12, 8, 2],
            [10, 6, 10, 4, 13, 10, 13, 6],
            [1, 10, 12, 15, 7, 6, 13, 8],
            [10, 10, 8, 5, 1, 6, 9, 4],
            [12, 11, 6, 41, 5, 10, 2, 7],
            [1, 8, 7, 40, 7, 14, 14, 3],
            [95, 14, 14, 14, 3, 15, 53, 45]]

    print(*tab, sep='\n')
    
    print(solution(tab, 4, 4), end='\n\n')

    tab = [[15, 6, 1, 5, 13, 2, 13, 12],
            [7, 14, 9, 6, 8, 12, 8, 2],
            [10, 6, 10, 4, 13, 10, 13, 6],
            [1, 10, 12, 15, 7, 6, 13, 8],
            [10, 10, 8, 5, 1, 6, 9, 4],
            [12, 11, 6, 41, 5, 10, 2, 7],
            [1, 8, 7, 40, 7, 14, 14, 3],
            [5, 14, 14, 14, 3, 15, 53, 45]]

    print(*tab, sep='\n')
    
    print(solution(tab, 4, 4))