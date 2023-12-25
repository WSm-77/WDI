# Zadanie 25. Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca wskaźnik do
# ostatniego elementu przed cyklem.

import usefuleFunctions as uf

def last_element_before_cycle(g) -> uf.Node:
    fast = g.next
    slow = g.next
    while True:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break
        #end if
    #end while
    fast = g
    while fast.next is not slow:
        fast = fast.next
        slow = slow.next
    #end while
    return fast

if __name__ == "__main__":
    tab = [i for i in range(1, 10 + 1)]
    myList = uf.list_to_linked_list_with_cycle(tab, 4 - 1)  # 4 is start of cycle
    print(last_element_before_cycle(myList).val)

    myList = uf.list_to_linked_list_with_cycle(tab, 7 - 1)  # 7 is start of cycle
    print(last_element_before_cycle(myList).val)