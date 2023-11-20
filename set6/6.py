def min_sum_of_elements_and_indexes(T, index=0, numberOfElements=0, sumOfElements=0, sumOfIndexes=0, minNumberOfElements=float('inf')):
    # print("index:", index, "number of elements:", numberOfElements, "sum of ele:", sumOfElements, "sum of ind:", sumOfIndexes)
    if sumOfElements == sumOfIndexes and numberOfElements > 0:
        return sumOfElements if numberOfElements < minNumberOfElements else None
            
    if index == len(T):
        return None
    else:
        case1 = min_sum_of_elements_and_indexes(T, index + 1, numberOfElements, sumOfElements, sumOfIndexes)
        case2 = min_sum_of_elements_and_indexes(T, index + 1, numberOfElements + 1, sumOfElements + T[index], sumOfIndexes + index)
        if case1 != None:
            return case1
        elif case2 != None:
            return case2
        else:
            return None
    
if __name__ == "__main__":
    tab = [ 1,7,3,5,11,2 ]
    print(min_sum_of_elements_and_indexes(tab))