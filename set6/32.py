def solution(T, k, index = 0, set1 = 0, set2 = 0, numberOfUsedElements = 0):
    if index == len(T):
        return True if numberOfUsedElements == k and set1 == set2 else False
    #end if

    currentElement = T[index]
    if solution(T, k, index + 1, set1, set2, numberOfUsedElements) or \
       solution(T, k, index + 1, set1 + currentElement, set2, numberOfUsedElements + 1) or \
       solution(T, k, index + 1, set1, set2 + currentElement, numberOfUsedElements + 1):
        return True
    #end if

    return False

if __name__ == "__main__":
    tab = [1,10,11,3,40,5,10,2]
    k = 3
    print(solution(tab, k))