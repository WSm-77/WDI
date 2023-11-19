def find_ns(T, n, currentProduct, used, index=0):
    if n == 0 or index == len(T):
        if currentProduct == 1:
            print("used:", end=' ')
            for u in used:
                print(u[0], end=' ')
            #end for
            print("\tat indexes:", end=' ')
            for u in used:
                print(u[1], end=' ')
            #end for
            print()
        #end if
        return
    #end if

    currentNum = T[index]
    if currentProduct % currentNum == 0:
        used.append((currentNum, index))
        find_ns(T, n - 1, currentProduct // currentNum, used, index + 1)
        used.pop()
    #end if
    find_ns(T, n, currentProduct, used, index + 1)

if __name__ == "__main__":
    tab = [7,12,7,15,12,2,3,2,3,4,7,45,4,9,10,5]
    targetProduct = 180
    n = 3
    used = []
    find_ns(tab, n, targetProduct, used)