# Zadanie 6. Proszę napisać funkcję wstawiającą na koniec listy nowy element. Do funkcji należy przekazać
# wskazanie na pierwszy element listy oraz wstawianą wartość.

import usefuleFunctions as uf

def append(ptr, element):
    if ptr == None:
        ptr = uf.Node(element)
        return ptr
    #end if
    begining = ptr
    while ptr.next != None:
        ptr = ptr.next
    #end while
    ptr.next = uf.Node(element)
    return begining

if __name__ == "__main__":
    tab = [4,2,6,1,6,7,2]
    linkedList = None
    for ele in tab:
        linkedList = append(linkedList, ele)
        uf.print_list(linkedList)
    #end for