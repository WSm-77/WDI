# Zadanie 31. Proszę napisać funkcję, która rozdziela listę na dwie listy. Pierwsza powinna zawierać klucze
# parzyste dodatnie, drugi klucze nieparzyste ujemne, pozostałe elementy należy usunąć z pamięci. Do funkcji
# należy przekazać wskaźniki na listę z danymi oraz wskaźniki na listy wynikowe. Funkcja powinna zwrócić
# liczbę usuniętych elementów.

import usefuleFunctions as uf

def special_remove(oldList, newLists) -> int:
    l1 = uf.Node()
    l2 = uf.Node()
    ptr1 = l1
    ptr2 = l2
    removedCnt = 0
    while oldList != None:
        if oldList.val > 0 and oldList.val % 2 == 0:
            ptr1.next = oldList
            ptr1 = ptr1.next
        elif oldList.val < 0 and oldList.val % 2 == 1:
            ptr2.next = oldList
            ptr2 = ptr2.next
        else:
            removedCnt += 1
        #end if
        tmp = oldList.next
        oldList.next = None
        oldList = tmp
    #end while
    newLists.append((l1.next, l2.next))
    return removedCnt

if __name__ == "__main__":
    tab = [2, 3,5,1,3, -3,4, 3, 6,-1,-7,-9,8]
    oldList = uf.remove_guradian(uf.list_to_linked_list(tab))
    uf.print_list(oldList)
    newLists = []
    print(f"removed {special_remove(oldList, newLists)} elements")
    for ele in newLists:
        for ptr in ele:
            uf.print_list(ptr)
        #end for
    #end for