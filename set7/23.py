# Zadanie 23. Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę elementów
# w cyklu.

import usefuleFunctions as uf

def length_of_cycle(g) -> int:
    fast = g.next
    slow = g.next
    while True:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break
        #end if
    #end while
    fast = g.next
    while fast is not slow:
        fast = fast.next
        slow = slow.next
    #end while
        
    elemsInCycle = 0
    while True:
        slow = slow.next
        elemsInCycle += 1
        if slow is fast:
            break
        #end if
    #end while

    return elemsInCycle

if __name__ == "__main__":
    tab = [1,2,3,4,5,6,7,8,9]
    myList = uf.list_to_linked_list_with_cycle(tab, 3)          # 4 is start of cycle
    print(length_of_cycle(myList))

    tab = [9,8,7,6,5,4,3,2,1]
    myList = uf.list_to_linked_list_with_cycle(tab, 6)          # 3 is start of cycle
    print(length_of_cycle(myList))