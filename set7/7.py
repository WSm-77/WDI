# Zadanie 7. Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji należy przekazać wskazanie
# na pierwszy element listy.

import usefuleFunctions as uf

def pop(ptr):
    if ptr == None:
        return None
    elif ptr.next == None:
        return None
    originalPtr = ptr
    while ptr.next.next != None:
        ptr = ptr.next
    #end while
    ptr.next = None
    return originalPtr

if __name__ == "__main__":
    tab = [4,2,6,1,6,7,2]
    linkedList = uf.remove_guradian(uf.list_to_linked_list(tab))
    uf.print_list(linkedList)
    for i in range(8):
        linkedList = pop(linkedList)
        uf.print_list(linkedList)