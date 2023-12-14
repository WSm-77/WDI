class Node:
    def __init__(self, my_next, my_val) -> None:
        self.next = my_next
        self.val = my_val

def reverse_rek(current, prev = None):
    if current == None:
        return prev
    
    nextElement = current.next
    current.next = prev

    return reverse_rek(nextElement, current)

def reverse_it(current, prev = None):
    while current != None:
        nextElement = current.next
        current.next = prev
        prev = current
        current = nextElement
    return prev

def print_list(first):
    while first != None:
        print(first.val)
        first = first.next
    #end while

if __name__ == "__main__":
    elements = [Node(None, i + 1) for i in range(5)]
    first = elements[0]

    for i in range(4):
        elements[i].next = elements[i + 1]
    #end for
    elements[4] = None

    print_list(first)

    first = reverse_rek(first)

    print("reversed:")
    print_list(first)

    first = reverse_it(first)

    print("re-reversed:")
    print_list(first)