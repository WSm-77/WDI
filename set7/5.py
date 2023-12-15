# Zadanie 5. Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do 10 list, według ostatniej cyfry pola val. W drugim kroku powstałe listy należy połączyć w jedną listę odsyłaczową, która jest
# posortowana niemalejąco według ostatniej cyfry pola val.

class Node:
    def __init__(self, v = None) -> None:
        self.val = v
        self.next = None

def sort_by_last_digit(ptr):
    result = ptr
    lastDigitListsBeg = [Node() for _ in range(10)]
    lastDigitListsPtr = [lastDigitListsBeg[i] for i in range(10)]
    
    while ptr != None:
        lastdigit = ptr.val % 10
        lastDigitListsPtr[lastdigit].next = Node(ptr.val)
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

def append(ptr, element):
    if ptr == None:
        ptr = Node(element)
        return ptr
    #end if
    begining = ptr
    while ptr.next != None:
        ptr = ptr.next
    #end while
    ptr.next = Node(element)
    return begining

def print_list(ptr):
    print("your list:")
    if ptr == None:
        print("list is empty")
    result = ''
    i = 20
    while ptr != None and i > 0:
        print(ptr.val, end=' ')
        result += str(ptr.val) + ', '
        ptr = ptr.next
        i -= 1
    #end while
    print()
    # print(result.rstrip(', '))
        
if __name__ == "__main__":
    tab = [41,22,64,11,64,73,20,100,57,29,83]
    linkedList = None
    for ele in tab:
        linkedList = append(linkedList, ele)
    #end for
    print_list(linkedList)
    linkedList = sort_by_last_digit(linkedList)
    print_list(linkedList)