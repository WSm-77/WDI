def sequence(T):
    N = len(T)
    min_end, max_start = float('inf'), 0
    length = 1
    for i in range(N - 1):
        if T[i + 1] > T[i]:
            length += 1
        else:
            if length > 2:
                max_start = max(max_start, T[i - length + 1])
                min_end = min(min_end, T[i])
            #end if
            length = 1
        #end if
    #end for
    if length > 2:
        max_start = max(max_start, T[i - length + 1])
        min_end = min(min_end, T[i])
    #end if
    return max_start > min_end

if __name__ == "__main__":
    tab = [2,15,17,13,17,19,23,2,6,4,8,3,5,7,1,3,2]

    print(sequence(tab))

    tab = [2,15,17,13,17,19,23,2,6,4,8,3,5,7,14,3,2]

    print(sequence(tab))