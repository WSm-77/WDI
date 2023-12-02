def eight_queens_problem():
    chessBoard = [[0 for _ in range(8)] for _ in range(8)]
    found = False

    def updateChessBoard(chessBoard, R, C, increment):
        moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for move in moves:
            nextR = R + move[0]
            nextC = C + move[1]
            while 0 <= nextR < 8 and 0 <= nextC < 8:
                chessBoard[nextR][nextC] += increment
                nextR += move[0]
                nextC += move[1]
            #end while
        #end for
    #end def

    def rek(chessBoard, R=0):
        nonlocal found
        if R == 8:
            # print(*chessBoard, sep='\n')
            for x in range(8):
                for y in range(8):
                    if chessBoard[x][y] == 0:
                        print('Q ', end='')
                    else:
                        print('# ',end='')
                    #end if
                #end for
                print()
            #end for
            found = True
            return True
        #end if

        for C in range(8):
            if chessBoard[R][C] == 0:
                updateChessBoard(chessBoard, R, C, 1)
                if rek(chessBoard, R + 1):
                    return True
                #end if
                updateChessBoard(chessBoard, R, C, -1)
            #end if
        #end for

        return False
    
    rek(chessBoard)

if __name__ == "__main__":
    eight_queens_problem()