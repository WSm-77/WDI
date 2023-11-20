def min_sum_of_elements_and_indexes(T, index=0, numberOfElements=0, sumOfElements=0, sumOfIndexes=0):
    # print("index:", index, "number of elements:", numberOfElements, "sum of ele:", sumOfElements, "sum of ind:", sumOfIndexes)
    if sumOfElements == sumOfIndexes and numberOfElements > 0:
        return numberOfElements
    if index == len(T):
        return float('inf')
    else:
        return min(min_sum_of_elements_and_indexes(T, index + 1, numberOfElements, sumOfElements, sumOfIndexes), \
                    min_sum_of_elements_and_indexes(T, index + 1, numberOfElements + 1, sumOfElements + T[index], sumOfIndexes + index))
    
if __name__ == "__main__":
    tab = [ 1,7,3,5,11,2 ]
    print(min_sum_of_elements_and_indexes(tab))