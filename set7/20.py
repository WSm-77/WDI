# Zadanie 20. Dana jest lista zawierająca ciąg obustronnie domkniętych przedziałów. Krańce przedziałów
# określa uporządkowana para liczb całkowitych. Proszę napisać stosowne deklaracje oraz funkcję redukującą
# liczbę elementów listy. Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17] powinien zostać zredukowany
# do listy: [13,19] [2,6] [7,12]

import usefuleFunctions as uf


def consolidate(interval1, interval2) -> tuple:
    if interval1[1] - interval1[0] > interval2[1] - interval2[0]:
        interval1, interval2 = interval2, interval1
    #end if
    intersection = interval1
    modified = False
    if interval2[0] <= interval1[0] <= interval2[1]:
        modified = True
        intersection = (interval2[0], max(interval1[1], interval2[1]))
    elif interval2[0] <= interval1[1] <= interval2[1]:
        modified = True
        intersection = (min(interval1[0], interval2[0]), interval2[1])
    #end if
    return intersection, modified

def reduce(g):
    modified = True
    while modified:
        modified = False
        ptr = g
        while ptr.next != None:
            secondPtr = g
            changed = False
            currentInterval = ptr.next.val
            while secondPtr is not ptr:
                intersection, doIntersect = consolidate(currentInterval, secondPtr.next.val)
                if doIntersect:
                    modified = changed = True
                    secondPtr.next.val = intersection
                    break
                #end if
                secondPtr = secondPtr.next
            #end while
            if changed:
                tmp = ptr.next
                ptr.next = ptr.next.next
                tmp.next = None
            else:
                ptr = ptr.next
            #end if
        #end while
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