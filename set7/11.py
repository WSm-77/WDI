# Zadanie 11. Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do której przekazujemy
# wskaźnik na początek oraz wartość klucza. Jeżeli element o takim kluczu występuje w liście należy go usunąć
# z listy. Jeżeli elementu o zadanym kluczu brak w liście należy element o takim kluczu wstawić do listy

class Node:
    def __init__(self, k = None, n = None) -> None:
        self.key = k
        self.next = n

def at_key(g, key):
    start = g
    while g.next != None:
        if g.next.key == key:
            tmp = g.next
            g.next = g.next.next
            tmp.next = None
            return start
        #end if
        g = g.next
    #end while
    g.next = Node(key, None)
    return start

####################
# helper functions #
####################

def init_guradian_list():
    return Node(None, None)

def print_guradian_list(ptr):
    print("GUARDIAN", end=' -> ')
    while ptr.next != None:
        print(ptr.next.key, end=' -> ')
        ptr = ptr.next
    #end while
    print("END")

if __name__ == "__main__":
    myList = init_guradian_list()
    
    print("key:", 5)
    myList = at_key(myList, 5)
    print_guradian_list(myList)

    print("key:", 1)
    myList = at_key(myList, 1)
    print_guradian_list(myList)

    print("key:", 2)
    myList = at_key(myList, 2)
    print_guradian_list(myList)

    print("key:", 5)
    myList = at_key(myList, 5)
    print_guradian_list(myList)

    print("key:", 3)
    myList = at_key(myList, 3)
    print_guradian_list(myList)

    print("key:", 1)
    myList = at_key(myList, 1)
    print_guradian_list(myList)
    