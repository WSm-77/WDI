# Zadanie 20. Dana jest lista zawierająca ciąg obustronnie domkniętych przedziałów. Krańce przedziałów
# określa uporządkowana para liczb całkowitych. Proszę napisać stosowne deklaracje oraz funkcję redukującą
# liczbę elementów listy. Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17] powinien zostać zredukowany
# do listy: [13,19] [2,6] [7,12]

import usefuleFunctions as uf

# def do_intercect(interval1, interval2):
#     return interval2[0] <= interval1[0] <= interval2[1] or interval2[0] <= interval1[1] <= interval2[1]

def consolidate(interval1, interval2) -> tuple:
    intersection = interval1
    if interval2[0] <= interval1[0] <= interval2[1]:
        intersection = (interval2[0], max(interval1[1], interval2[1]))
    elif interval2[0] <= interval1[1] <= interval2[1]:
        intersection = (min(interval1[0], interval2[0]), interval2[1])
    #end if
    return intersection

def reduce(g):
    ptr = g
    while ptr.next != None:
        secondPtr = g
        changed = False
        tmp1 = tmp2 = uf.Node()
        currentInterval = ptr.next.val
        while secondPtr is not ptr:
            intersection = consolidate(currentInterval, secondPtr.next.val)
            if intersection != currentInterval:
                changed = True
                secondPtr.next.val = intersection
                currentInterval = intersection
                thirdPtr = secondPtr.next

                # thirdPtr is used new interval intersects more than one of previosuly checked intervals
                while thirdPtr is not ptr:
                    intersection = consolidate(currentInterval, thirdPtr.next.val)
                    if intersection != currentInterval:
                        secondPtr.next.val = intersection
                        if thirdPtr.next is not ptr:
                            tmp = thirdPtr.next
                            thirdPtr.next = thirdPtr.next.next
                            tmp.next = None
                        else:
                            changed2 = True
                        #end if
                        break
                    #end if
                    thirdPtr = thirdPtr.next
                #end while
                    
                break
            #end if
            secondPtr = secondPtr.next
        #end while
        # uf.print_guradian_list(g)
        if changed:
            if changed2:
                tmp = ptr
                ptr = ptr.next
                tmp.next = None
                tmp = ptr
                ptr = ptr.next
                tmp.next = None
            else:
                tmp = ptr.next
                ptr.next = ptr.next.next
                tmp.next = None
            #end if
        else:
            ptr = ptr.next
        #end if
    #end while
    return g

if __name__ == "__main__":
    tab = [(15,19), (2,5), (7,11), (8,12), (5,6), (13,17)]
    myList = uf.list_to_linked_list(tab)
    uf.print_guradian_list(myList)
    myList = reduce(myList)
    uf.print_guradian_list(myList)

    tab = [(15,19), (2,5), (4,16), (20,21)]
    # for i in range(len(tab) - 1):
    #     for j in range(i + 1, len(tab)):
    #         print(tab[i], tab[j], consolidate(tab[i], tab[j]))
    # #end for
    
    myList = uf.list_to_linked_list(tab)
    uf.print_guradian_list(myList)
    myList = reduce(myList)
    uf.print_guradian_list(myList)