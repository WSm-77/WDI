def isValid(T, firstIndex, length, div):
    for i in range(length):
        if T[firstIndex + i] / T[firstIndex + i + length] != div:
            return False
        #end if
    #end for
    return True

def sequence(T):
    N = len(T)
    for l in range(3, N // 2):
        for firstIndex in range(N - 2 * l + 1):
            if isValid(T, firstIndex, l, T[firstIndex] / T[firstIndex + l]):
                return (firstIndex, firstIndex + l - 1)
            #end if
        #end for
    #end for
    return (0,0)


if __name__ == "__main__":
    T =  [2,5,7,3,2,3,5,7,6,9,15,21,17,19,23,2,6,4,8,3,5,7,1,3,2]

    print(sequence(T))