# Zadanie 18. Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy unikalne. Do funkcji
# należy przekazać wskazanie na pierwszy element listy.

import usefuleFunctions as uf

def remove_repeated(g) -> uf.Node:
    start = g
    while g.next != None:
        currentVal = g.next.val
        ptr = g.next
        while ptr.next != None:
            if ptr.next.val == currentVal:
                tmp = ptr.next
                ptr.next = ptr.next.next
                tmp.next = None
            else:
                ptr = ptr.next
            #end if
        #end whie
        g = g.next
    #end while
    return start

if __name__ == "__main__":
    tab = [1,2,3,2,2,4,5,5,4,6,2,3,1,7,8]
    myList = uf.list_to_linked_list(tab)
    uf.print_guradian_list(myList)
    myList = remove_repeated(myList)
    uf.print_guradian_list(myList)