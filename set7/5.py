# Zadanie 5. Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do 10 list, według ostatniej cyfry pola val. W drugim kroku powstałe listy należy połączyć w jedną listę odsyłaczową, która jest
# posortowana niemalejąco według ostatniej cyfry pola val.

import usefuleFunctions as uf

def sort_by_last_digit(ptr):
    result = ptr
    lastDigitListsBeg = [uf.Node() for _ in range(10)]
    lastDigitListsPtr = [lastDigitListsBeg[i] for i in range(10)]
    
    while ptr != None:
        lastdigit = ptr.val % 10
        lastDigitListsPtr[lastdigit].next = uf.Node(ptr.val)
        lastDigitListsPtr[lastdigit] = lastDigitListsPtr[lastdigit].next
        ptr = ptr.next
    # end while

    for i in range(9):
        if lastDigitListsPtr[i] != lastDigitListsBeg[i]:
            for j in range(i + 1,10):
                if lastDigitListsBeg[j].next != None:
                    lastDigitListsPtr[i].next = lastDigitListsBeg[j].next
                    break

    for i in range(9, -1, -1):                          # "delocating" memory
        if lastDigitListsBeg[i].next != None:
            result = lastDigitListsBeg[i].next
            lastDigitListsBeg[i].next = None
        #end if
    #end for
    return result
        
if __name__ == "__main__":
    tab = [41,22,64,11,64,73,20,100,57,29,83]
    linkedList = uf.remove_guradian(uf.list_to_linked_list(tab))
    uf.print_list(linkedList)
    linkedList = sort_by_last_digit(linkedList)
    uf.print_list(linkedList)