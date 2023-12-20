class Node:
    def __init__(self, v = None, n = None) -> None:
        self.val = v
        self.next = n

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

    newElement = Node(string, g.next)
    g.next = newElement
    
    return True

####################
# helper functions #
####################

def print_guradian_list(ptr):
    print("GUARDIAN", end=' -> ')
    while ptr.next != None:
        print(ptr.next.val, end=' -> ')
        ptr = ptr.next
    #end while
    print("END")

def init_guradian_list():
    return Node(None, None)

if __name__ == "__main__":
    tab = ['ala','ma','malego','kota','i','duzego','psa','ma','mama','ps','kota','duzego']
    myList = init_guradian_list()
    for ele in tab:
        print("string:", add_string(myList, ele))
    #end for
    print_guradian_list(myList)
