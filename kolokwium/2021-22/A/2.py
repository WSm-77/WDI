def compatible(num1, num2):
    digs = [0 for _ in range(4)]
    while num1 > 0:
        digs[num1 % 4] = 1
        num1 //= 4
    #end while
    while num2 > 0:
        lastDig = num2 % 4
        if digs[lastDig] > 0:
            digs[lastDig] = 2
        else:
            return False
        #end if
        num2 //= 4
    #end while
    for i in range(4):
        if digs[i] == 1:
            return False
        #end if
    #end for
    return True

def main2(T):
    N = len(T)
    maxLen = 0
    for i in range(N - 1):
        for r in range(1, N - i):
            if compatible(T[i], T[i + r]):
                currentLen = 2
                for k in range(i + 2*r, N, r):
                    if compatible(T[i], T[k]):
                        currentLen += 1
                        maxLen = max(maxLen, currentLen)
                    else:
                        break
                    #end if
                #end for
            #end if
        #end for
    #end for
    return maxLen

if __name__ == '__main__':
    tab = [2,13,6,23,8,13,7,23,9]

    print(main2(tab))