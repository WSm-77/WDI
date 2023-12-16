# Zadanie 1. Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze struktury listy odsyłaczowej.
# 1. czy element należy do zbioru
# 2. wstawienie elementu do zbioru
# 3. usunięcie elementu ze zbioru

class Node:
    def __init__(self, v = None, n = None) -> None:
        self.val = v
        self.next = n

def member(ptr, element):
    while ptr != None and ptr.val < element:
        ptr = ptr.next
    #end while
    return ptr != None and ptr.val == element

def add(head, element):
    originalFirst = head
    tail = None
    while head != None and head.val < element:
        tail = head
        head = head.next
    #end while
    if head != None and head.val == element:
        return  originalFirst
    
    newElement = Node(element)
    
    if tail == None:                #adding at begening of the list
        newElement.next = head
        originalFirst = newElement
    else:                           #adding in middle of the list
        newElement.next = head
        tail.next = newElement
    #end if

    return originalFirst

def remove(head, element):
    originalFirst = head
    tail = None
    while head != None and head.val < element:
        tail = head
        head = head.next
    #end while

    if head == None:                #no such element in the list
        return originalFirst
    #end if

    if head.val == element:
        if tail != None:
            tail.next = head.next
        else:
            originalFirst = head.next
        #end if
        head.next = None
    #end if

    return originalFirst

def print_list(ptr):
    print("your list:")
    if ptr == None:
        print("list is empty")
        return
    while ptr != None:
        print(ptr.val, end=' -> ')
        ptr = ptr.next
    #end while
    print('END')
        
##########################
# solution with guardian #
##########################
        
def init_guradian_list():
    return Node(None, None)

def print_guradian_list(ptr):
    print("GUARDIAN", end=' -> ')
    while ptr.next != None:
        print(ptr.next.val, end=' -> ')
        ptr = ptr.next
    #end while
    print("END")

def guardian_member(ptr, ele):
    while ptr.next != None and ptr.next.val < ele:
        ptr = ptr.next
    #end while
    return ptr.next.val == ele

def guardian_add(ptr, ele):
    start = ptr
    while ptr.next != None and ptr.next.val < ele:
        ptr = ptr.next
    #end while
    if ptr.next == None or ptr.next.val != ele:
        newElement = Node(ele, ptr.next)
        ptr.next = newElement
    #end if
    return start

def guardian_remove(ptr, ele):
    start = ptr
    while ptr.next != None and ptr.next.val < ele:
        ptr = ptr.next
    #end while
    if ptr.next != None and ptr.next.val == ele:
        tmp = ptr.next
        ptr.next = ptr.next.next
        tmp.next = None
    #end if
    return start

if __name__ == "__main__":
    tab = [11,5,2,3,7,13]
    first = None

    print_list(first)
    for ele in tab:
        first = add(first, ele)
    #end for
    print_list(first)

    first = remove(first, 5)
    first = remove(first, 11)
    first = remove(first, 10)

    print("after removing:")
    print_list(first)

    ############# with guradian ###############

    print("\n\nguradina solution:\n\n")

    tab = [11,5,2,3,7,13,2,2,2]
    l1 = init_guradian_list()
    print_guradian_list(l1)
    for ele in tab:
        l1 = guardian_add(l1, ele)
    #end for
    print_guradian_list(l1)

    x = 3
    print(f"is {x} member:", guardian_member(l1, x))
    x = 5
    print(f"is {x} member:", guardian_member(l1, x))
    x = 4
    print(f"is {x} member:", guardian_member(l1, x))

    print("removing...")
    for ele in tab[2:5]:
        l1 = guardian_remove(l1, ele)
    #end for
    print_guradian_list(l1)

    x = 3
    print(f"is {x} member:", guardian_member(l1, x))
    x = 5
    print(f"is {x} member:", guardian_member(l1, x))
    x = 4
    print(f"is {x} member:", guardian_member(l1, x))