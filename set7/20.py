# Zadanie 20. Dana jest lista zawierająca ciąg obustronnie domkniętych przedziałów. Krańce przedziałów
# określa uporządkowana para liczb całkowitych. Proszę napisać stosowne deklaracje oraz funkcję redukującą
# liczbę elementów listy. Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17] powinien zostać zredukowany
# do listy: [13,19] [2,6] [7,12]

import usefuleFunctions as uf


def consolidate(interval1, interval2) -> tuple:
    intersection = interval1
    if interval2[0] <= interval1[0] <= interval2[1]:
        intersection = (interval2[0], max(interval1[1], interval2[1]))
    elif interval2[0] <= interval1[1] <= interval2[1]:
        intersection = (min(interval1[0], interval2[0]), interval2[1])
    #end if
    return intersection

def reduce(g):
    firstPtr = g.next
    firstPrev = g
    while firstPtr != None:
        secondPtr = g.next
        changed = 0
        currentInterval = firstPtr.val
        while secondPtr is not firstPtr:
            intersection = consolidate(currentInterval, secondPtr.val)
            if intersection != currentInterval:
                changed = 1
                secondPtr.val = intersection
                currentInterval = intersection
                thirdPrev = secondPtr
                thirdPtr = secondPtr.next

                # thirdPtr is used new interval intersects more than one of previosuly checked intervals
                while thirdPtr is not firstPtr:
                    intersection = consolidate(currentInterval, thirdPtr.val)
                    if intersection != currentInterval:
                        secondPtr.val = intersection
                        if thirdPtr.next is not firstPtr:
                            thirdPrev.next = thirdPtr.next
                            thirdPtr.next = None
                        else:
                            firstPrev = thirdPrev
                            thirdPrev.next = firstPtr.next
                            firstPtr = firstPtr.next
                            thirdPtr.next.next = None
                            thirdPtr.next = None
                            changed = 2
                        #end if
                        break
                    #end if
                    thirdPrev = thirdPtr
                    thirdPtr = thirdPtr.next
                #end while
                    
                break
            #end if
            secondPtr = secondPtr.next
        #end while
        match changed:
            case 0:
                firstPrev = firstPtr
                firstPtr = firstPtr.next
            case 1:
                firstPrev.next = firstPtr.next
                firstPtr.next = None
                firstPtr = firstPrev.next
            case 2:
                pass
        #end match
    #end while
    return g

if __name__ == "__main__":
    tab = [(15,19), (2,5), (7,11), (8,12), (5,6), (13,17)]
    myList = uf.list_to_linked_list(tab)
    uf.print_guradian_list(myList)
    myList = reduce(myList)
    uf.print_guradian_list(myList)

    tab = [(15,19), (2,5), (4,16), (20,21)]
    myList = uf.list_to_linked_list(tab)
    uf.print_guradian_list(myList)
    myList = reduce(myList)
    uf.print_guradian_list(myList)

    tab = [(1,2), (3,4), (5,6), (7,8), (1, 20)]
    myList = uf.list_to_linked_list(tab)
    uf.print_guradian_list(myList)
    myList = reduce(myList)
    uf.print_guradian_list(myList)