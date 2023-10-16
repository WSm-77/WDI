EPS = 1e-10

# def factorial(n):
#     if n == 0:
#         return 1
    
#     factorial = 1

#     for i in range (1, n + 1):
#         factorial *= i
    
#     return factorial

def claculateEulerConst():
    coutner = 2
    factorial = 2
    e = 2
    e_previous = 0
    
    while abs(e - e_previous) > EPS:
        e_previous = e
        e += 1/factorial
        # print(e)
        coutner += 1
        factorial *= coutner

    return e

if __name__ == '__main__':
    print("Euler Constant:", claculateEulerConst())