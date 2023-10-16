from math import sqrt

EPS = 1e-10

def bisection(n):
    x_top = sqrt(n)
    x_bottom = 0
    assert(x_top ** x_top > n)
    while abs(x_top - x_bottom) > EPS:
        pom = (x_bottom + x_top) / 2
        # print(pom)
        if pom ** pom < n:
            x_bottom = pom
        else:
            x_top = pom
        print("bottom:", x_bottom)
        print("top:",x_top)
    return x_top
            


if __name__ == "__main__":
    print(bisection(2023))
    x = 4.832263384741964
    print(x**x)