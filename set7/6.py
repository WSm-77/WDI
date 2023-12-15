# Zadanie 6. Proszę napisać funkcję wstawiającą na koniec listy nowy element. Do funkcji należy przekazać
# wskazanie na pierwszy element listy oraz wstawianą wartość.

class Node:
    def __init__(self, v) -> None:
        self.val = v
        self.next = None

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

def print_list(first):
    print("your list:")
    while first != None:
        print(first.val)
        first = first.next
    #end while

if __name__ == "__main__":
    tab = [4,2,6,1,6,7,2]
    linkedList = None
    for ele in tab:
        linkedList = append(linkedList, ele)
        print_list(linkedList)
    #end for