from math import isqrt

def is_complex(number):
    if number < 4:
        return False
    if number % 2 == 0:
        return True
    
    div = 3
    iroot = isqrt(number)
    while div <= iroot:
        if number % div == 0:
            return True
        
        div += 2
    #end while
    return False

def build_numbers(A, B):
    def rek(A, B, number=1):
        if A == B == 0:
            return 1 if is_complex(number) else 0
        #end if
        result = 0
        if A > 0:
            result += rek(A - 1, B, number * 2 + 1)
            #end if
        if B > 0:
            result += rek(A, B - 1, number * 2)
        #end if
        return result
    #end def
    return rek(A - 1, B)

if __name__ == "__main__":
    print(build_numbers(2, 3))
    print(build_numbers(3, 3))