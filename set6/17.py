from math import isqrt

def isPrime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0 or num % 3 == 0:
        return False
    div = 5
    iroot = isqrt(num)
    while div < iroot:
        if num % div == 0:
            return False
        
        div += 2
        if num % div == 0:
            return False
        div += 4
    #end while
    return True

def solution(num1, num2, number=0, power=1):
    if num1 == num2 == 0:
        return 1 if isPrime(number) else 0
    
    result = 0
    if num1 != 0:
        result += solution(num1//10, num2, number + power * (num1 % 10), power * 10)
        
    if num2 != 0:
        result += solution(num1, num2//10, number + power * (num2 % 10), power * 10)
    
    return result

if __name__ == "__main__":
    number1 = 23
    number2 = 17

    print(solution(number1, number2))

    number1 = 73
    number2 = 19

    print(solution(number1, number2))