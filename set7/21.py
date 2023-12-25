# Zadanie 21. Kolejne elementy listy o zwiększającej się wartości pola val nazywamy podlistą rosnącą.
# Proszę napisać funkcję, która usuwa z listy wejściowej najdłuższą podlistę rosnącą. Warunkiem usunięcia
# jest istnienie w liście dokładnie jednej najdłuższej podlisty rosnącej.

import usefuleFunctions as uf

def remove_longest_increasing_sequence(g) -> uf.Node:
    currentPtr = g.next
    currentStart = g            # pointer to 1 element before current start
    maxSeqStart = g
    maxLength = 0
    isTheLongest = True
    while currentPtr != None:
        currentLen = 1
        while currentPtr.next != None and currentPtr.next.val > currentPtr.val:
            currentLen += 1
            currentPtr = currentPtr.next
        #end while
        if currentLen == maxLength:
            isTheLongest = False
        elif currentLen > maxLength:
            maxLength = currentLen
            isTheLongest = True
            maxSeqStart = currentStart
        #end if
        currentStart = currentPtr
        currentPtr = currentPtr.next
    #end while
    if isTheLongest:
        for _ in range(maxLength):
            tmp = maxSeqStart.next
            maxSeqStart.next = maxSeqStart.next.next
            tmp.next = None
        #end for
    #end if
    return g

if __name__ == "__main__":
    tab = [1,2,3, 1,2,3,4,5, 1,2,3,4, 1,2,3]
    print("longest seqence: 1,2,3,4,5")
    myList = uf.list_to_linked_list(tab)
    uf.print_guradian_list(myList)
    remove_longest_increasing_sequence(myList)
    uf.print_guradian_list(myList)

    print("longest seqence: doesn't exist")
    tab = [1,2,3, 1,2,3,4, 1,2,3,4, 1,2,3]
    myList = uf.list_to_linked_list(tab)
    uf.print_guradian_list(myList)
    remove_longest_increasing_sequence(myList)
    uf.print_guradian_list(myList)