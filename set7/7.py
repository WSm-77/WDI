# Zadanie 7. Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji należy przekazać wskazanie
# na pierwszy element listy.

class Node:
    def __init__(self, v) -> None:
        self.val = v
        self.next = None

def pop(ptr):
    if ptr == None:
        return None
    elif ptr.next == None:
        return None
    originalPtr = ptr
    while ptr.next.next != None:
        ptr = ptr.next
    #end while
    ptr.next = None
    return originalPtr

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
    while ptr != None:
        result += str(ptr.val) + ', '
        ptr = ptr.next
    #end while
    print(result.rstrip(', '))

if __name__ == "__main__":
    tab = [4,2,6,1,6,7,2]
    linkedList = None
    for ele in tab:
        linkedList = append(linkedList, ele)
    #end for
    print_list(linkedList)
    for i in range(8):
        linkedList = pop(linkedList)
        print_list(linkedList)