# Zadanie 9. Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne elementy listy przechowują
# kolejne cyfry. Proszę napisać funkcję zwiększającą taką liczbę o 1.

class Node:
    def __init__(self, v) -> None:
        self.val = v
        self.next = None

def increment_number(ptr):
    def rek(ptr):
        if ptr == None:
            return 1
        
        ptr.val += rek(ptr.next)
        if ptr.val == 10:
            ptr.val -= 10
            return 1
        return 0
    #end def

    if rek(ptr) == 1:
        newElement = Node(1)
        newElement.next = ptr
        ptr = newElement
    #end if
    return ptr

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

def print_number(ptr):
    print("your number:")
    if ptr == None:
        print("list is empty")
    result = ''
    while ptr != None:
        print(ptr.val, end='')
        ptr = ptr.next
    #end while
    print()

if __name__ == "__main__":
    num = [4,2,6,1,5,7,9]
    linkedList = None
    for ele in num:
        linkedList = append(linkedList, ele)
    #end for
    print_number(linkedList)
    linkedList = increment_number(linkedList)
    print_number(linkedList)
   
    num = [1,2,3,4,1]
    linkedList = None
    for ele in num:
        linkedList = append(linkedList, ele)
    #end for
    print_number(linkedList)
    linkedList = increment_number(linkedList)
    print_number(linkedList)

    num = [9,9,9,9]
    linkedList = None
    for ele in num:
        linkedList = append(linkedList, ele)
    #end for
    print_number(linkedList)
    linkedList = increment_number(linkedList)
    print_number(linkedList)