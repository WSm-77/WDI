# Zadanie 24. Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę elementów
# przed cyklem.

import usefuleFunctions as uf

def number_of_elems_before_cycle(g) -> int:
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
    beforeCycle = 0
    while fast is not slow:
        beforeCycle += 1
        fast = fast.next
        slow = slow.next
    #end while
    return beforeCycle

if __name__ == "__main__":
    tab = [i for i in range(1, 10 + 1)]
    myList = uf.list_to_linked_list_with_cycle(tab, 4 - 1)  # 4 is start of cycle
    print(number_of_elems_before_cycle(myList))

    myList = uf.list_to_linked_list_with_cycle(tab, 7 - 1)  # 7 is start of cycle
    print(number_of_elems_before_cycle(myList))