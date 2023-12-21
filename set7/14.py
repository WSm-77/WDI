import usefuleFunctions as uf

def remove_following_if_divideable_by_current(g) -> uf.Node:
    if g.next == None:
        return g
    #end if
    ptr = g.next
    prev = g
    while ptr.next != None:
        currentValue = ptr.val
        nextValue = ptr.next.val
        if nextValue % currentValue == 0:
            prev.next = ptr.next
            tmp = ptr
            ptr = ptr.next
            tmp.next = None
        else:
            prev = ptr
            ptr = ptr.next
        #end if
    #end while 
    return g

if __name__ == '__main__':
    num = [5,2,4,5,3,6,7]
    num1 = uf.list_to_linked_list(num)
    uf.print_guradian_list(num1)
    num1 = remove_following_if_divideable_by_current(num1)
    uf.print_guradian_list(num1)

    num = [2,4,8,16,32,64]
    num1 = uf.list_to_linked_list(num)
    uf.print_guradian_list(num1)
    num1 = remove_following_if_divideable_by_current(num1)
    uf.print_guradian_list(num1)