from math import e, log

EPS = 1e-6

def f(x):
    return x**x - 2023

def df(x):
    return  (x**x)*(log(x,e) + 1) 

def solution():
    x = 3
    x_prev = 0
    while abs(x_prev - x) > EPS:
        x_prev = x
        x = x - f(x)/df(x)
    #end while
    return x

if __name__ == "__main__":
    print(solution())