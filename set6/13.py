def print_all_summands(number, used=[], usedIndex=0):
    if number < 0:
        print("wrong number!!!")
        return
    if number == 0:
        print(*used, sep='+', end='\n')
        return
    
    minElem = 1

    if usedIndex != 0:
        minElem = used[usedIndex - 1]

    for summand in range(minElem, number + 1):
            used.append(summand)
            print_all_summands(number - summand, used, usedIndex + 1)
            used.pop()

if __name__ == "__main__":
    print_all_summands(6)