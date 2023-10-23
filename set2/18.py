def printAn(upperLimit = 1000):
    n = 0
    a_prev = 0
    a_next = 1
    b_prev = 2
    b_next = 2
    while a_next < 1000:
        print(f"a{n} = {a_prev}")
        print(f"b{n} = {b_prev}")
        print()
        a_prev, a_next, b_prev, b_next = a_next, a_next - (b_next * a_prev), b_next, b_next + 2 * a_prev
        n += 1
    #end while

if __name__ == "__main__":
    # printAn()
    n = 0
    a_prev = 0
    a_next = 1
    b_prev = 2
    b_next = 2
    while True:
        an = int(input(f"enter a{n}: "))
        if an == a_prev:
            print(f"b{n} = {b_prev}")
        else:
            print("wrong number!!!")
            break
        a_prev, a_next, b_prev, b_next = a_next, a_next - (b_next * a_prev), b_next, b_next + 2 * a_prev
        n += 1
    #end while