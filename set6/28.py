def number_of_ones(number):
    result = 0
    while number > 0:
        result += number % 2
        number //= 2
    #end while
    return result

# each "set" is int type variable that stores number of "1" used in binary to represent all numbers assined to set 
def is_divideable(T, index = 0, set1 = 0, set2 = 0,set3 = 0):
    if index == len(T):
        return set1 == set2 == set3
    
    numberOfOnes = number_of_ones(T[index])
    return is_divideable(T, index + 1, set1 + numberOfOnes, set2, set3) or \
            is_divideable(T, index + 1, set1, set2 + numberOfOnes, set3) or \
            is_divideable(T, index + 1, set1, set2, set3 + numberOfOnes)
#end def

if __name__ == "__main__":
    tab = [2, 3, 5, 7, 15]
    print(tab)
    print(is_divideable(tab))

    tab = [5, 7, 15]
    print(tab)
    print(is_divideable(tab))