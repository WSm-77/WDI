# Zadanie 29. Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby naturalne. W obu listach
# liczby są posortowane rosnąco. Proszę napisać funkcję usuwającą z każdej listy liczby nie występujące w
# drugiej. Do funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić łączną liczbę usuniętych
# elementów.

import usefuleFunctions as uf

def remove_not_contained_by_second_list(ptr1, ptr2) -> int:
    removedCnt = 0
    while ptr1.next != None and ptr2.next != None:
        if ptr1.next.val < ptr2.next.val:
            removedCnt += 1
            tmp = ptr1.next
            ptr1.next = ptr1.next.next
            tmp.next = None
        elif ptr1.next.val > ptr2.next.val:
            removedCnt += 1
            tmp = ptr2.next
            ptr2.next = ptr2.next.next
            tmp.next = None
        else:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        #end if
    #end while
            
    if ptr1.next == None:
        ptr1 = ptr2
    #end if

    while ptr1.next != None:
            removedCnt += 1
            tmp = ptr1.next
            ptr1.next = ptr1.next.next
            tmp.next = None
    #end while
    return removedCnt

if __name__ == "__main__":
    tab = [2,5,6,7,9]
    l1 = uf.list_to_linked_list(tab)
    tab = [1,3,4,5,6]
    l2 = uf.list_to_linked_list(tab)
    uf.print_guradian_list(l1)        
    uf.print_guradian_list(l2)

    print(f"removed: {remove_not_contained_by_second_list(l1,l2)} elements")

    uf.print_guradian_list(l1)        
    uf.print_guradian_list(l2)

