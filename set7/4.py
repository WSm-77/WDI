class Node:
    def __init__(self, my_next, my_val) -> None:
        self.next = my_next
        self.val = my_val

def reverse(current, prev = None):
    if current == None:
        return prev
    
    nextElement = current.next
    current.next = prev

    return reverse(nextElement, current)

if __name__ == "__main__":
    elements = [Node(None, i + 1) for i in range(5)]
    first = elements[0]

    for i in range(4):
        elements[i].next = elements[i + 1]
    #end for
    elements[4] = None

    firstCp = first
    while firstCp != None:
        print(firstCp.val)
        firstCp = firstCp.next
    #end while

    first = reverse(first)

    print("reversed:")

    firstCp = first
    while firstCp != None:
        print(firstCp.val)
        firstCp = firstCp.next
    #end while