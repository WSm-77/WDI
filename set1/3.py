def isInFib(number):
    fib1 = fib2 = 1
    sum = 0

    while sum < number:
        sum += fib1
        fib1, fib2 = fib2, fib1 + fib2
    #end while

    fib1 = fib2 = 1

    while sum > number:
        sum -= fib1
        fib1, fib2 = fib2, fib1 + fib2
    #end while

    return sum == number

if __name__ == "__main__":
    number = int(input("enter number: "))
    if isInFib(number):
        print("yes")
    else:
        print("no")