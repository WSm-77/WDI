def min_sum_of_elements_and_indexes(T):
    minNumberOfElements=float('inf')
    used = []
    def rek(index, numberOfElements, sumOfElements, sumOfIndexes, used):
        # print(used)
        print("index:", index, "number of elements:", numberOfElements, "sum of ele:", sumOfElements, "sum of ind:", sumOfIndexes, used)
        if sumOfElements == sumOfIndexes and numberOfElements > 0:
            nonlocal minNumberOfElements
            if numberOfElements < minNumberOfElements:
                minNumberOfElements = numberOfElements
                return sumOfElements
            else: 
                return None
                
        if index == len(T):
            return None
        else:
            case1 = rek(index + 1, numberOfElements, sumOfElements, sumOfIndexes, used)
            case2 = rek(index + 1, numberOfElements + 1, sumOfElements + T[index], sumOfIndexes + index, used + [index])
            if case1 != None:
                return case1
            elif case2 != None:
                return case2
            else:
                return None
        #end if
    #end def
    return rek(0,0,0,0, used)
    
if __name__ == "__main__":
    tab = [ 1,7,3,5,11,2 ]
    print(min_sum_of_elements_and_indexes(tab))