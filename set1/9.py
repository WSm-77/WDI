from math import sqrt

def printDividers(number):
    root = sqrt(number)
    counter = 1
    while counter < root:
        if number % counter == 0:
            print(counter)
            print(number // counter)
        counter += 1
    #end while
    if counter ** 2 == number:
        print(counter)



if __name__ == "__main__":
    number = int(input("enter number: "))
    printDividers(number)