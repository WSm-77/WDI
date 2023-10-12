from math import sqrt

def main():
    number=399999989999
    # number=12341
    if 0==number%2:
        print("ERROR: number can not be even!!!")
    while True:
        next=getNextNumberWithSum101(number)
        if isPrime(next):
            print(next)
            break
        number=next

def getNextNumberWithSum101(n):
    while True:
        n+=18
        print("n =", n)
        if 101==sumOfDigits(n):
            print("return")
            return n

def isPrime(n):
    b=3
    root=sqrt(n)
    if n%2==0:
        return False
    else:
        while b<=root:
            if n%b==0:
                return False
            else:
                b+=2
        return True    

def sumOfDigits(n):
    sum=0
    while 0!=n:
        sum+=n%10
        n = n // 10
    # print(sum)
    return sum

# def main():
#     i=299999999999
#     while True:
#         if(isPrime(i)):
#             print(i)
#             if(sumOfDigits(i) == 101):
#                 print(i)
#                 break
#         i+=2

# def replace_char(string, index, new_char):
#     new_string = string[:index] + new_char + string[index+1:]
#     return new_string



main()