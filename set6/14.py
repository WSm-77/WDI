def move_block(blockSize, fromStart, toEnd):
    print("move block", blockSize, "from", fromStart, "to", toEnd, )

def tower_of_hanoi(blockSize, A, B, C):
    if blockSize < 1:
        print("wrong tower height!!!")
        return
    if blockSize == 1:
        move_block(1, A, C)
        return
    else:
        tower_of_hanoi(blockSize - 1, A, C, B)
        move_block(blockSize, A, C)
        tower_of_hanoi(blockSize - 1, B, C, A)

if __name__ == "__main__":
    n = int(input("Enter tower height: "))
    tower_of_hanoi(n, 'A', 'B', 'C')