# Zadanie 12. Zbiór mnogościowy zawierający napisy jest reprezentowany w postaci jednokierunkowej listy.
# Napisy w łańcuchu są uporządkowane leksykograficznie. Proszę napisać stosowne definicje typów oraz funkcję
# dodającą napis do zbioru. Do funkcji należy przekazać wskaźnik do listy oraz wstawiany napis, funkcja
# powinna zwrócić wartość logiczną wskazującą, czy w wyniku operacji moc zbioru uległa zmianie.

import usefuleFunctions as uf

def compare_strings(str1, str2) -> bool:                # returns 1 if first string is "bigger", 0 if strings are the same, -1 otherwise
    str1Len = len(str1)
    str2Len = len(str2)
    n = str1Len
    lenCompare = None
    if str1Len == str2Len:
        lenCompare = 0
    elif str1Len > str2Len:
        n = str2Len
        lenCompare = 1
    else:
        lenCompare = -1
    #end if
    for i in range(n):
        str1Ascii = ord(str1[i])
        str2Ascii = ord(str2[i])
        if str1Ascii > str2Ascii:
            return 1
        elif str1Ascii < str2Ascii:
            return -1
        #end if
    #end for

    return lenCompare

def add_string(g, string) -> bool:
    while g.next != None:
        match compare_strings(string, g.next.val):
            case 1:
                g = g.next
            case 0:
                return False
            case -1:
                break
        #end match
    #end while

    newElement = uf.Node(string, g.next)
    g.next = newElement
    
    return True

if __name__ == "__main__":
    tab = ['ala','ma','malego','kota','i','duzego','psa','ma','mama','ps','kota','duzego']
    myList = uf.init_guradian_list()
    for ele in tab:
        print("string:", add_string(myList, ele))
    #end for
    uf.print_guradian_list(myList)
