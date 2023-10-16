def main():
    n = int(input("eneter number: "))
    print(newtonSqrt(n))

def newtonSqrt(n):
    approximation = n * 0.5
    newtonSqrt = n
    while abs(approximation-newtonSqrt) > 1e-10:
        newtonSqrt = approximation
        approximation = 0.5*(approximation + n/(approximation))
    #end
    return approximation

main()