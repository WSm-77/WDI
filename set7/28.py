# Zadanie 28. Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby naturalne. W pierwszej liście
# liczby są posortowane rosnąco, a w drugiej nie. Proszę napisać funkcję usuwającą z obu list liczby występujące
# w obu listach. Do funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić łączną liczbę
# usuniętych elementów.

import usefuleFunctions as uf

def remove_repeated(g1, g2) -> int:
    ptr1 = g1
    removedCnt = 0
    while ptr1.next != None:
        ptr2 = g2
        removed = False
        while ptr2.next != None:
            if ptr2.next.val == ptr1.next.val:
                removed = True
                removedCnt += 1
                tmp = ptr2.next
                ptr2.next = ptr2.next.next
                tmp.next = None
            else:
                ptr2 = ptr2.next
            #end if
        #end while
        if removed:
            removedCnt += 1
            tmp = ptr1.next
            ptr1.next = ptr1.next.next
            tmp.next = None
        else:
            ptr1 = ptr1.next
        #end if
    #end while
    return removedCnt


if __name__ == "__main__":

    ########## first test ##########

    print("first test")

    tab = [i for i in range(1, 10)]
    l1 = uf.list_to_linked_list(tab)
    uf.print_guradian_list(l1)

    tab = [4,1,6,2,3,2]
    l2 = uf.list_to_linked_list(tab)
    uf.print_guradian_list(l2)

    print("removed:", remove_repeated(l1, l2), "elements")
    uf.print_guradian_list(l1)
    uf.print_guradian_list(l2)

    ########## second test ##########

    print("second test")

    tab = [i for i in range(1, 10, 2)]
    l1 = uf.list_to_linked_list(tab)
    uf.print_guradian_list(l1)

    tab = [4,1,6,2,3,2]
    l2 = uf.list_to_linked_list(tab)
    uf.print_guradian_list(l2)

    print("removed:", remove_repeated(l1, l2), "elements")
    uf.print_guradian_list(l1)
    uf.print_guradian_list(l2)