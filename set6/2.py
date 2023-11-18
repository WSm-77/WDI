from math import sqrt
from random import randint

def diff_divs(num):
    if num < 2:
        return 0
    #end if
    cnt = 0
    div = 2
    divideable = False
    while num != 1:
        while num % div == 0:
            num //= div
            divideable = True
        #end while
        if divideable:
            cnt += 1
        #end if
        div += 1
    #end while
    return cnt
    
def number_weight(T, weight1=0, weight2=0, weight3=0, index=0):
    if index == len(T):
        return weight1 == weight2 == weight3
    else:
        currnetNumWeight = diff_divs(T[index])
        index += 1
        return number_weight(T, weight1 + currnetNumWeight, weight2, weight3, index) or \
                number_weight(T, weight1, weight2 + currnetNumWeight, weight3, index) or \
                number_weight(T, weight1, weight2, weight3 + currnetNumWeight, index)
    
if __name__ == "__main__":
    tab =  [randint(1,15) for i in range(11)]
    print(tab)
    print(number_weight(tab))
    
    tab =  [2,3,4,6,5]
    print(tab)
    print(number_weight(tab))