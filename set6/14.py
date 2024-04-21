from collections import deque

def move_block(blockSize, fromStart, toEnd):
    print("move block", blockSize, "from", fromStart, "to", toEnd, )

def tower_of_hanoi_rek(blockSize, A, B, C):
    if blockSize < 1:
        print("wrong tower height!!!")
        return
    if blockSize == 1:
        move_block(1, A, C)
        return
    else:
        tower_of_hanoi_rek(blockSize - 1, A, C, B)
        move_block(blockSize, A, C)
        tower_of_hanoi_rek(blockSize - 1, B, A, C)

# toDo: 0 - tower_of_hanoi (add to stack), 1 - print move
def tower_of_hanoi_it(towerSize, source, destination, through):
    if towerSize < 1:
        print("wrong tower size!!!")
        return
    #end if

    # blockSize, from, to, with_help_of
    stack = deque()
    stack.append((towerSize, source, destination, through, 0))
    movesCnt = 0

    while stack:
        blockSize, source, destination, through, toDo = stack.pop()

        match toDo:
            case 0:
                if blockSize == 1:
                    move_block(blockSize, source, destination)
                    movesCnt += 1
                else:
                    stack.append((blockSize - 1, through, destination, source, 0))
                    stack.append((blockSize, source, destination, None, 1))
                    stack.append((blockSize - 1, source, through, destination, 0))

            case 1:
                move_block(blockSize, source, destination)
                movesCnt += 1
    #end while

    return movesCnt

if __name__ == "__main__":
    n = int(input("Enter tower height: "))
    print("recursively:")
    tower_of_hanoi_rek(n, 'A', 'B', 'C')
    
    print("\niteratively:")
    print(f"to solve hanoi tower made of {n} blocks you need to do {tower_of_hanoi_it(n, 'A', 'C', 'B')} moves")