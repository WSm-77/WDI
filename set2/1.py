from math import isqrt

#this function checks if "number" is in Fibonacci sequence
def inFibSeq(number):
    a = 1
    b = 1
    while b < number:
        a, b = b, a + b
    #end while
    return b == number

def isResultOfMultiplication(number):
    isResult = False
    fib1 = 0
    fib2 = 1
    iroot = isqrt(number)
    while fib2 <= iroot:
        fib1, fib2 = fib2, fib1 + fib2
        # print(fib2, number//fib2)

        if number % fib2 != 0:
            continue

        if inFibSeq(number//fib2):
            isResult = True
            break

    #end while
    print(fib2, number//fib2)
    return isResult

if __name__ == "__main__":
    num = int(input("enter number: "))
    print(isResultOfMultiplication(num))
