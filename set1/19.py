EPS = 1e-10

##################
# first solution #
##################

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

###################
# second solution #
###################

def calculateE():
    e = 0.0
    an = 1.0
    cntr = 1
    while an > EPS:
        e += an
        an /= cntr
        cntr += 1
    #end while
    return e

if __name__ == '__main__':
    print("Euler Constant (first solution):", claculateEulerConst())
    print("Euler Constant (second solution):", calculateE())