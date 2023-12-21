# Zadanie 8. Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi element listy. Do funkcji
# należy przekazać wskazanie na pierwszy element listy.

import usefuleFunctions as uf

def remove_every_second_element(ptr):
    originalPtr = ptr
    tail = None
    cntr = 0
    while ptr != None:
        tail = ptr
        ptr = ptr.next
        if cntr % 2 == 0 and ptr != None:
            tmp = ptr
            ptr = ptr.next
            tail.next = ptr
            tmp.next = None
        #end if
    #end while
    return originalPtr

if __name__ == "__main__":
    tab = [4,2,6,1,5,7,2]
    linkedList = uf.remove_guradian(uf.list_to_linked_list(tab))
    uf.print_list(linkedList)
    linkedList = remove_every_second_element(linkedList)
    uf.print_list(linkedList)