from math import isqrt

def solution(number):
    div1 = isqrt(number)
    while True:
        if number % div1 == 0:
            break
        else:
            div1 -= 1

    #end while
    return div1, number // div1



if __name__ == "__main__":
    assert(solution(25) == (5, 5))
    assert(solution(24) == (4, 6))
    number = int(input("enter number: "))
    myTuple = solution(number)
    print(f"{number} = {myTuple[0]} * {myTuple[1]}")