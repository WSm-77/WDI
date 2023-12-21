# Zadanie 9. Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne elementy listy przechowują
# kolejne cyfry. Proszę napisać funkcję zwiększającą taką liczbę o 1.

import usefuleFunctions as uf

def increment_number(g):
    def rek(ptr):
        if ptr == None:
            return 1
        #end if
        ptr.val += rek(ptr.next)
        if ptr.val == 10:
            ptr.val -= 10
            return 1
        return 0
    #end def

    if rek(g.next) == 1:
        g.next = uf.Node(1, g.next)
    #end if
    return g

if __name__ == "__main__":
    num = [4,2,6,1,5,7,9]
    linkedList = uf.list_to_linked_list(num)
    print("before increment:", end=' ')
    uf.print_guradian_number(linkedList, myEnd=' ')
    linkedList = increment_number(linkedList)
    print("after increment:", end=' ')
    uf.print_guradian_number(linkedList)
   
    num = [1,2,3,4,1]
    linkedList = uf.remove_guradian(uf.list_to_linked_list(num))
    print("before increment:", end=' ')
    uf.print_guradian_number(linkedList, myEnd=' ')
    linkedList = increment_number(linkedList)
    print("after increment:", end=' ')
    uf.print_guradian_number(linkedList)

    num = [9,9,9,9]
    linkedList = uf.remove_guradian(uf.list_to_linked_list(num))
    print("before increment:", end=' ')
    uf.print_guradian_number(linkedList, myEnd=' ')
    linkedList = increment_number(linkedList)
    print("after increment:", end=' ')
    uf.print_guradian_number(linkedList)