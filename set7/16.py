# Zadanie 16. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy jednokierunkowej, 
# przenosi na początek listy te z nich, które mają parzystą ilość piątek w zapisie ósemkowym.

import usefuleFunctions as uf

def even_number_of_5_in_octal(num):
    cnt5 = 0
    while num > 0:
        if num % 8 == 5:
            cnt5 += 1
        #end if
        num //= 8
    #end while
    return cnt5 % 2 == 0

def move_to_beginning(g) -> uf.Node:
    if g.next == None:
        return g
    # end if
    endOf5Odd = g
    ptr = g.next
    prev = g
    while ptr != None:
        if even_number_of_5_in_octal(ptr.val):
            if endOf5Odd.next is ptr:
                prev = endOf5Odd = ptr
                ptr = ptr.next
            else:
                tmp = ptr.next
                ptr.next = endOf5Odd.next
                endOf5Odd.next = ptr
                endOf5Odd = endOf5Odd.next
                ptr = tmp
                prev.next = ptr
            #end if
        else:
            prev = ptr
            ptr = ptr.next
        #end if
    #end while
    return g

if __name__ == "__main__":
    tab = [i for i in range(15)]
    for i in range(len(tab)):
        print(f"does {tab[i]} have odd number of 5 in octal:", even_number_of_5_in_octal(tab[i]))
    #end for
    myList = uf.list_to_linked_list(tab)
    uf.print_guradian_list(myList)
    myList = move_to_beginning(myList)
    uf.print_guradian_list(myList)

    tab = [5,13,21,1,2,3,5,5,7,5,6]
    for i in range(len(tab)):
        print(f"does {tab[i]} have odd number of 5 in octal:", even_number_of_5_in_octal(tab[i]))
    #end for
    myList = uf.list_to_linked_list(tab)
    uf.print_guradian_list(myList)
    myList = move_to_beginning(myList)
    uf.print_guradian_list(myList)