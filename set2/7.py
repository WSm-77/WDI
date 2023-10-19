def isInAnSeq(number):
    result = False
    n = 1
    An = 3
    while An <= number:
        if number % An == 0:
            result = True
            break
        #end if
        An = n*n + n + 1
        n += 1
    #end while

    # print("An:",An)
    # print("An-1:", ((n-2)*(n-2) + (n-2) + 1))

    return result

if __name__ == "__main__":
    assert(isInAnSeq(3))
    assert(isInAnSeq(243))
    assert(isInAnSeq(7))
    assert(isInAnSeq(62))
    assert(not isInAnSeq(2))
    assert(not isInAnSeq(5))
    
    number = int(input("enter number: "))
    if isInAnSeq(number):
        print(f"{number} is multiplicity of An sequence")
    else:
        print(f"{number} is not mulitplicity of An sequence")
    #end if
#end if