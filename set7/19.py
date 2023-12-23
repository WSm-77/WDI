# Zadanie 19. Elementy w liście są uporządkowane według wartości klucza. Proszę napisać funkcję usuwającą z listy elementy o nieunikalnym kluczu. Do funkcji przekazujemy wskazanie na pierwszy element listy,
# funkcja powinna zwrócić liczbę usuniętych elementów.

from random import randint
import usefuleFunctions as uf

def remove_repeated(g) -> uf.Node:
    ptr = g
    while ptr.next != None:
        currentVal = ptr.next.val
        secondPtr = ptr.next
        while secondPtr.next != None and secondPtr.next.val == currentVal:
            tmp = secondPtr.next
            secondPtr.next = secondPtr.next.next
            tmp.next = None
        #end while
        if ptr.next != None:
            ptr = ptr.next
        #end if
    #end while
    return g

if __name__ == "__main__":
    tab = [randint(1,7) for _ in range(15)]
    tab.sort()
    myList = uf.list_to_linked_list(tab)
    uf.print_guradian_list(myList)
    myList = remove_repeated(myList)
    uf.print_guradian_list(myList)