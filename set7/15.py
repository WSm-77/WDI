# Zadanie 15. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy jednokierunkowej, usuwa z niej wszystkie elementy, w których wartość klucza w zapisie trójkowym ma większą
# ilość jedynek niż dwójek.

import usefuleFunctions as uf

def more_1_than_2_in_trinary(num):
    cnt = [0 for _ in range(3)]
    while num > 0:
        rest = num % 3
        cnt[rest] += 1
        num //= 3
    #end while
    return cnt[1] > cnt[2]

def special_remove(g) -> uf.Node:
    if g.next == None:
        return g
    #end if
    prev = g
    ptr = g.next
    while ptr != None:
        if more_1_than_2_in_trinary(ptr.val):
            prev.next = ptr.next
            tmp = ptr
            ptr = ptr.next
            tmp.next = None
        else:
            prev = ptr
            ptr = ptr.next
        #end if
    #end while
    return g

if __name__ == "__main__":
    num = [14,1,14,2,14,14,3,14]
    num1 = uf.list_to_linked_list(num)
    uf.print_guradian_list(num1)
    num1 = special_remove(num1)
    uf.print_guradian_list(num1)

    num = [i for i in range(15)]
    num1 = uf.list_to_linked_list(num)
    uf.print_guradian_list(num1)
    num1 = special_remove(num1)
    uf.print_guradian_list(num1)