def calculateE(precision):
    e = [0 for _ in range(precision + 1)]
    an = [0 for _ in range(precision + 1)]
    an[0] = 1
    denominator = 1
    flag = True
    while flag:
        for i in range(precision, -1, -1):
            e[i] += an[i]
            if (e[i] > 9 ) and (i != 0):
                e[i] -= 10
                e[i-1] += 1
            #end if
        #end for
        rest = 0
        flag = False
        for j in range(precision + 1):
            an[j] += rest * 10
            rest = an[j] % denominator
            an[j] //= denominator
            if an[j] != 0:
                flag = True
        #end for
        denominator += 1
    #end while
    return e

if __name__ == "__main__":
    precision = 1000
    my_e = calculateE(precision)
    my_e.insert(1,".")
    print(*my_e, sep="")