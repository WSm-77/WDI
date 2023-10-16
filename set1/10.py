from math import sqrt

def isExcellentNumber(number):
    sum = 1
    counter = 2
    root = sqrt(number)
    while counter < root:
        if number % counter == 0:
            sum += counter
            sum += number // counter
        counter += 1
    if counter ** 2 == number:
        sum += counter
    # print("sum:", sum)
    if sum == number:
        return True
    else:
        return False
    
if __name__ == "__main__":
    for i in range(1, 1000000 + 1, 1):
        if isExcellentNumber(i):
            print(i, "is excellent")