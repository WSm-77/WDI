class Node:
    def __init__(self, v) -> None:
        self.val = v
        self.next = None

def add(head, element):
    originalFirst = head
    tail = None
    while head != None and head.val < element:
        tail = head
        head = head.next
    #end while
    
    newElement = Node(element)
    
    if tail == None:                #adding at begening of the list
        newElement.next = head
        originalFirst = newElement
    else:                           #adding in middle of the list
        newElement.next = head
        tail.next = newElement
    #end if

    return originalFirst

#########################
# first (easy) solution #
#########################

def merge_lists_easy(list1, list2):
    newList = None
    while list1 != None:
        newList = add(newList, list1.val)
        list1 = list1.next
    #end while
    while list2 != None:
        newList = add(newList, list2.val)
        list2 = list2.next
    #end while

    return newList

###################
# second solution #
###################

def merge_lists_it(list1, list2):
    assert(list1 != None and list2 != None)
    mergedList = None
    if list1.val < list2.val:
        firstElement = Node(list1.val)
        mergedList = firstElement
        list1 = list1.next
    else:
        firstElement = Node(list2.val)
        mergedList = firstElement
        list2 = list2.next
    #end if
    currentPtr = mergedList
    while list1 != None or list2 != None:
        while list1 != None and list1.val < list2.val:
            newElement = Node(list1.val)
            currentPtr.next = newElement
            currentPtr = newElement
            list1 = list1.next
        #end while
        while list2 != None and list2.val <= list1.val:
            newElement = Node(list2.val)
            currentPtr.next = newElement
            currentPtr = newElement
            list2 = list2.next
        #end while
    #end while
    return mergedList

def merge_lists_rek(list1, list2):
    if list1 == list2 == None:
        return None
    
    newElement = None

    if list1 != None and (list2 == None or list1.val < list2.val):
        newElement = Node(list1.val)
        list1 = list1.next
        newElement.next = merge_lists_rek(list1, list2)
    else:
        newElement = Node(list2.val)
        list2 = list2.next
        newElement.next = merge_lists_rek(list1, list2)
    #end if

    return newElement

def print_list(ptr):
    print("your list:")
    if ptr == None:
        print("list is empty")
    result = ''
    while ptr != None:
        result += str(ptr.val) + ', '
        ptr = ptr.next
    #end while
    print(result.rstrip(', '))

if __name__ == "__main__":
    tab1 = [7,3,4,6,4,3]
    list1 = None
    for ele in tab1:
        list1 = add(list1, ele)
    #end for
    print_list(list1)

    tab2 = [7,8,3,5,2]
    list2 = None
    for ele in tab2:
        list2 = add(list2, ele)
    #end for
    print_list(list2)

    mergedListEasy = merge_lists_easy(list1, list2)
    print("easy merge")
    print_list(mergedListEasy)

    mergedListIt = merge_lists_easy(list1, list2)
    print("itterational merge")
    print_list(mergedListIt)

    mergedListRek = merge_lists_rek(list1, list2)
    print("recursive merge")
    print_list(mergedListRek)