import usefuleFunctions as uf

######################
# recursive solution #
######################

def remove_if_previous_is_smaller_rek(g) -> uf.Node:
    def rek(ptr, prev):
        if ptr == None:
            return None
        #end if

        tmp = rek(ptr.next, ptr)
        if prev.val > ptr.val:
            ptr.next = None
            return tmp
        else:
            ptr.next = tmp
            return ptr
        #end if
    #end def
    if g.next != None:
        g.val = -float('inf')
        g.next = rek(g.next, g)
        g.val = None
    return g

#########################
# itterational solution #
#########################

def remove_if_previous_is_smaller_it(g) -> uf.Node:
    g.val = prevValue = -float('inf')
    ptr = g.next
    prev = g
    while ptr != None:
        currentValue = ptr.val
        if currentValue < prevValue:
            prev.next = ptr.next
            tmp = ptr
            ptr = ptr.next
            tmp.next = None
        else:
            prev = ptr
            ptr = ptr.next
        #end if
        prevValue = currentValue
    #end while
    g.val = None
    return g

if __name__ == "__main__":
    tab = [3,4,5,2,6,7,3,2,1]
    ptr = uf.list_to_linked_list(tab)
    uf.print_guradian_list(ptr)
    ptr = remove_if_previous_is_smaller_it(ptr)
    uf.print_guradian_list(ptr)

    tab = [7,6,5,4,3,2,1]
    ptr = uf.list_to_linked_list(tab)
    uf.print_guradian_list(ptr)
    ptr = remove_if_previous_is_smaller_rek(ptr)
    uf.print_guradian_list(ptr)