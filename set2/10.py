def isMultiplicityOfAn(number):
    result = False
    A_next = 2
    while A_next <= number:
        if number % A_next == 0:
            result = True
            break
        A_next = 3 * A_next + 1
        #end if
    #end while
    print(A_next)
    return result



if __name__ == "__main__":
    number = int(input("enter number: "))
    if isMultiplicityOfAn(number):
        print("this number is multiplicity of An")
    else:
        print("this number is NOT multiplicity of An")