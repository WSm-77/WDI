from math import sqrt

EPS = 1e-6

def exercise20(a,b):
    while abs(a-b) > EPS:
        print(a,b)
        # a_previous, b_previous = a, b
        # a = sqrt(a_previous*b_previous)
        # b = (a_previous + b_previous)/2.0
        a, b= sqrt(a*b), (a + b)/2.0
    return a

if __name__ == '__main__':
    print(exercise20(1,5))