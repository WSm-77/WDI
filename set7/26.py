# Zadanie 26. Proszę napisać funkcję, która sprawdza czy jedna lista zawiera się w drugiej. Do funkcji należy
# przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wartość logiczną.

import usefuleFunctions as uf

def do_contain_help(ptr1, ptr2) -> bool:
    result = True
    while ptr2.next != None:
        if ptr1.next == None or ptr1.next.val != ptr2.next.val:
            result = False
            break
        #end if
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    #end while
    
    return result    

def do_contain(g1, g2) -> bool:
    ptr1 = g1
    ptr2 = g2

    if uf.guradian_list_len(g1) < uf.guradian_list_len(g2):
        ptr1, ptr2 = ptr2, ptr1
    #end if
        
    while ptr1.next != None:
        if do_contain_help(ptr1, ptr2):
            return True
        #end if
        ptr1 = ptr1.next
    #end while
    
    return False


if __name__ == "__main__":
    
    ######### first test #########

    tab = [2,3]
    l1 = uf.list_to_linked_list(tab)
    uf.print_guradian_list(l1)

    tab = [1,2,3,4,5,6,7]
    l2 = uf.list_to_linked_list(tab)
    uf.print_guradian_list(l2)
    print(do_contain(l1, l2))

    ######## second test ########

    tab = [2 for _ in range(10)]
    l1 = uf.list_to_linked_list(tab)
    uf.print_guradian_list(l1)

    tab = [1,2,3,4,5,6,7]
    l2 = uf.list_to_linked_list(tab)
    uf.print_guradian_list(l2)
    print(do_contain(l1, l2))