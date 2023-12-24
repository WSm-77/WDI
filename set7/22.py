# Zadanie 22. Dana jest lista, która być może zakończona jest cyklem. Napisać funkcję, która sprawdza ten fakt.

import usefuleFunctions as uf

def is_list_with_cycle(g) -> bool:
    fast = g
    slow = g
    result = None
    while True:
        if fast == None or fast.next == None:
            result = False
            break
        #end if
        fast = fast.next.next
        slow = slow.next 
        if fast is slow:
            result = True
            break
        #end if
    #end while
    return result

if __name__ == "__main__":
    tab = [1,2,3,4,5]
    myList = uf.list_to_linked_list_with_cycle(tab, 1)
    print(is_list_with_cycle(myList))
    myList = uf.list_to_linked_list(tab)
    print(is_list_with_cycle(myList))