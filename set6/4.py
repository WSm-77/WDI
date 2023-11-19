
def fill_with_knight_move(N):
    chessBoard = [[0 for _ in range(N)] for _ in range(N)]
    knight_moves = ((-2,1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
    found = False

    def possibleMove(next_R, next_C):
        return 0<= next_R < N and 0<= next_C < N and chessBoard[next_R][next_C] == 0
    #end def

    def move_knight(R, C, number):
        chessBoard[R][C] = number
        nonlocal found
        if number == N*N:
            print(*chessBoard, sep='\n', end='\n\n')
            found = True
            return
        for x,y in knight_moves:
            next_R = R + y
            next_C = C + x
            if possibleMove(next_R, next_C) and not found:
                move_knight(next_R, next_C, number + 1)
            #end if
        #end for
        chessBoard[R][C] = 0
    #end def

    move_knight(0, 0, 1)

if __name__ == "__main__":
    fill_with_knight_move(5)
    fill_with_knight_move(8)