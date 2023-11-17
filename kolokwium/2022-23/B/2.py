from math import isqrt

def exactly_2_diff_prime_divs(num):
    iroot = isqrt(num)
    div = 2
    cnt = 0
    while div <= iroot:
        if num % div == 0:
            cnt += 1
            while num % div == 0:
                num //= div
            #end while
        #end if
        div += 1
    #end while
    return cnt == 2

def sqare(T):
    N = len(T)
    for l in range(2, N - 1):
        for R in range(N - l + 1):
            for C in range(N - l + 1):
                product = T[R][C] * T[R + l - 1][C] * T[R][C + l - 1] * T[R + l - 1][C + l - 1]
                if exactly_2_diff_prime_divs(product):
                    return l,R,C
                #end if
            #end for
        #end for
    #end for
    return 0

if __name__ == "__main__":
    tab = [[4,5,3,4,6],
           [1,2,2,3,4],
           [3,50,3,2,5],
           [4,8,3,9,3],
           [7,7,7,7,7]]
    
    print(sqare(tab))