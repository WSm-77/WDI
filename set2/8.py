#########################
##   first solution    ##
#########################

# this function returns next number that cannot be created as the sum of following numbers in Fibonacci sequence
def nextNotSum(number):
    if number < 9:
        return 9
    
    fibPrevious = 1
    fibNext = 1

    while fibNext <= number:
        fibNext, fibPrevious = fibPrevious + fibNext, fibNext
    #end while

    # if we were given with e.g. 16 then our sequence looks like that:
    # 1  1  2  3  5  8  13          16        21              22
    #                   ^           ^         ^               ^
    #                   |           |         |               |
    #             fibPrevious     number   fibNext          result
    #
    # now our solution is somewhere between 16 and 21 OR it is 22

    sum = 0
    result = fibNext + 1

    while sum - number < 2 and fibPrevious > 1:
        fibPrevious, fibNext = fibNext - fibPrevious, fibPrevious
        sum += fibPrevious
    #end while

    # after changes our sequence looks like that:
    # 1  1  2       3  5  8  13         16            17            18
    #       ^       ^                   ^             ^             ^
    #       |       |                   |             |             |
    #    fibPrev  fibNext              number    searched number    sum

    if fibPrevious > 1:
        result = sum - fibPrevious + 1
        if result <= number:
            result = number + 1    

    return result

#########################
##   second solution   ##
#########################

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

def nextNotSumV2(number):
    solution = number + 1
    while True:
        if isInFib(solution):
            solution += 1
        else:
            return solution
        

if __name__ == "__main__":
    number = int(input("enter number: "))
    print("version 1:", nextNotSum(number))
    print("version 2:", nextNotSumV2(number))
