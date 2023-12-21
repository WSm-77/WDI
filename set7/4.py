# Zadanie 4. Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca kolejność jej elementów.

import usefuleFunctions as uf

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

if __name__ == "__main__":
    elements = [i + 1 for i in range(8)]
    first = uf.remove_guradian(uf.list_to_linked_list(elements))

    uf.print_list(first)

    first = reverse_rek(first)

    print("reversed:")
    uf.print_list(first)

    first = reverse_it(first)

    print("re-reversed:")
    uf.print_list(first)