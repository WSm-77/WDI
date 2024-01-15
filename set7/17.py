# Zadanie 17. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy dwukierunkowej, usuwa z niej 
# wszystkie elementy, w których wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek.

import usefuleFunctions as uf

class Node:
    def __init__(self, v = None, p = None, n = None) -> None:
        self.val = v
        self.prev = p
        self.next = n


def list_to_bi_directional_list(tab) -> Node:
    N = len(tab)
    if N == 0:
        return None
    
    g = Node(tab[0], None, None)
    ptr = g
    for i in range(1,N):
        ptr.next = Node(tab[i], ptr, None)
        ptr = ptr.next
    #end for
    return g

def print_bi_directional_list(ptr) -> None:
    result = "END <- "
    while ptr != None:
        result += str(ptr.val) + ' <-> '
        ptr = ptr.next
    #end while
    result = result[:-5] + " -> END"
    print(result)

def is_number_of_1_in_binary_odd(num) -> bool:
    cnt1 = 0
    while num > 0:
        cnt1 += num % 2
        num //= 2
    #end while
    return cnt1 % 2 == 1

def special_remove(g) -> Node:
    if g == None:
        return None
    
    ptr = g
    while ptr != None:
        tmp = ptr.next
        if is_number_of_1_in_binary_odd(ptr.val):
            if ptr.next != None:
                ptr.next.prev = ptr.prev
            #end if
            if ptr.prev != None:
                ptr.prev.next = ptr.next
            else:
                g = ptr.next
            ptr.next = ptr.prev = None
        #end if
        ptr = tmp
    #end while
    return g

if __name__ == "__main__":
    tab = [i + 1 for i in range(10)]
    shouldBeRemoved = [ele for ele in tab if is_number_of_1_in_binary_odd(ele)]
    print("should be removed:", *shouldBeRemoved)
    print()
    myList = list_to_bi_directional_list(tab)
    print_bi_directional_list(myList)
    myList = special_remove(myList)
    print_bi_directional_list(myList)

