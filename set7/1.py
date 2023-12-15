# Zadanie 1. Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze struktury listy odsyłaczowej.
# 1. czy element należy do zbioru
# 2. wstawienie elementu do zbioru
# 3. usunięcie elementu ze zbioru

class Node:
    def __init__(self, v) -> None:
        self.val = v
        self.next = None

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
    while ptr != None:
        print(ptr.val)
        ptr = ptr.next
    #end while

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