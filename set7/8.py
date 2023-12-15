# Zadanie 8. Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi element listy. Do funkcji
# należy przekazać wskazanie na pierwszy element listy.


class Node:
    def __init__(self, v) -> None:
        self.val = v
        self.next = None

def remove_every_second_element(ptr):
    originalPtr = ptr
    tail = None
    cntr = 0
    while ptr != None:
        tail = ptr
        ptr = ptr.next
        if cntr % 2 == 0 and ptr != None:
            tmp = ptr
            ptr = ptr.next
            tail.next = ptr
            tmp.next = None
        #end if
    #end while
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
    tab = [4,2,6,1,5,7,2]
    linkedList = None
    for ele in tab:
        linkedList = append(linkedList, ele)
    #end for
    print_list(linkedList)
    linkedList = remove_every_second_element(linkedList)
    print_list(linkedList)