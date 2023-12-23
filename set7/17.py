# Zadanie 17. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy dwukierunkowej, usuwa z niej 
# wszystkie elementy, w których wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek.

import usefuleFunctions as uf

class Node:
    def __init__(self, v = None, p = None, n = None) -> None:
        self.val = v
        self.prev = p
        self.next = n


def list_to_bi_directional_list(tab) -> Node:
    g = Node()
    ptr = g
    for ele in tab:
        ptr.next = Node(ele, ptr, None)
        ptr = ptr.next
    #end for
    return g

def print_guradian_bi_directional_list(ptr) -> None:
    result = "END <- GUARDIAN <-> "
    while ptr.next != None:
        result += str(ptr.next.val) + ' <-> '
        ptr = ptr.next
    #end while
    result =result[:-5] + " -> END"
    print(result)

def is_number_of_1_in_binary_odd(num) -> bool:
    cnt1 = 0
    while num > 0:
        cnt1 += num % 2
        num //= 2
    #end while
    return cnt1 % 2 == 1

def special_remove(g) -> Node:
    ptr = g
    while ptr.next != None:
        if is_number_of_1_in_binary_odd(ptr.next.val):
            tmp = ptr.next
            if ptr.next.next != None:
                ptr.next.next.prev = ptr
            #end if
            ptr.next = ptr.next.next
            tmp.next = tmp.prev = None
        else:
            ptr = ptr.next
        #end if
    #end while
    return g

if __name__ == "__main__":
    tab = [i + 1 for i in range(10)]
    for i in range(len(tab)):
        isOdd = is_number_of_1_in_binary_odd(tab[i])
        myEnd = (' X\n' if isOdd else '\n')
        print("should be removed?", i + 1, not isOdd, end=myEnd)
    #end for
    print()
    myList = list_to_bi_directional_list(tab)
    print_guradian_bi_directional_list(myList)
    myList = special_remove(myList)
    print_guradian_bi_directional_list(myList)

