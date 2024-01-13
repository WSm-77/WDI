# Zadanie 30. Dane są dwie niepuste listy, z których każda zawiera niepowtarzające się elementy. Elementy
# w pierwszej liście są uporządkowane rosnąco, w drugiej elementy występują w przypadkowej kolejności.
# Proszę napisać funkcję, która z dwóch takich list stworzy jedną, w której uporządkowane elementy będą
# stanowić sumę mnogościową elementów z list wejściowych. Do funkcji należy przekazać wskazania na obie
# listy, funkcja powinna zwrócić wskazanie na listę wynikową. Na przykład dla list: 2 -¿ 3 -¿ 5 -¿7-¿ 11 8 -¿ 2
# -¿ 7 -¿ 4 powinna pozostać lista: 2 -¿ 3 -¿ 4 -¿ 5 -¿7-¿ 8 -¿ 11

import usefuleFunctions as uf

def merge(l1, l2) -> uf.Node:
    g = uf.Node(l1.val)
    g.next = l1
    while l2 != None:
        ptr = g
        while ptr.next != None and ptr.next.val <= l2.val:
            ptr = ptr.next
        #end while
        next = l2.next
        if ptr.val != l2.val:
            l2.next = ptr.next
            ptr.next = l2
        #end if
        l2 = next
    #end while
    return g.next
        

if __name__ == "__main__":
    
    ########## first test ##########

    print("first test:")

    tab = [2,3,5,7,11]
    l1 = uf.remove_guradian(uf.list_to_linked_list(tab))
    tab = [8,2,7,4]
    l2 = uf.remove_guradian(uf.list_to_linked_list(tab))
    uf.print_list(l1)
    uf.print_list(l2)

    newList = merge(l1, l2)
    print("merged lists:")
    uf.print_list(newList)

    ########## second test ##########

    print("\nsecond test:")

    tab = [2,3,5,7,11]
    l1 = uf.remove_guradian(uf.list_to_linked_list(tab))
    tab = [4,3,1,6,7,12]
    l2 = uf.remove_guradian(uf.list_to_linked_list(tab))
    uf.print_list(l1)
    uf.print_list(l2)

    newList = merge(l1, l2)
    print("merged lists:")
    uf.print_list(newList)