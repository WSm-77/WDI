# Zadanie 16. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy jednokierunkowej, 
# przenosi na początek listy te z nich, które mają parzystą ilość piątek w zapisie ósemkowym.

import usefuleFunctions as uf

def even_number_of_5_in_octal(num):
    cnt5 = 0
    while num > 0:
        if num % 5 == 0:
            cnt5 += 1
        #end if
        num //= 8
    #end while
    return cnt5 % 2 == 0

def move_to_beginning(g) -> uf.Node:
    ptr = g
    while ptr.next != None:
        if even_number_of_5_in_octal(ptr.next.val):
            tmp = ptr.next.next
            ptr.next.next = g.next
            g.next = ptr.next
            ptr.next = tmp
        else:
            ptr = ptr.next
        #end if
    #end while
    return g

if __name__ == "__main__":
    tab = [i for i in range(15)]
    for i in range(len(tab)):
        print(i, even_number_of_5_in_octal(tab[i]))
    #end for
    myList = uf.list_to_linked_list(tab)
    uf.print_guradian_list(myList)
    myList = move_to_beginning(myList)
    uf.print_guradian_list(myList)