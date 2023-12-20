# Zadanie 10. Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać funkcję dodającą
# dwie takie liczby. W wyniku dodawania dwóch liczb powinna powstać nowa lista.

class Node:
    def __init__(self, v=None, n=None) -> None:
        self.val = v
        self.next = n

def guradian_list_len(linkedList):
    cnt = 0
    while linkedList.next != None:
        cnt += 1
        linkedList = linkedList.next
    #end while
    return cnt

def add_numbers(num1, num2):
    num1Len = guradian_list_len(num1)
    num2Len = guradian_list_len(num2)
    if num1Len <= num2Len:                          # we make sure that num1 is bigger than num2
        num1Len, num2Len = num2Len, num1Len
        num1, num2 = num2, num1
    #end if
    lenDifference = num1Len - num2Len
    def add_rek(ptr1, ptr2, cnt):                   # to this function pass list WITHOUT guardian
        if ptr1 == None:
            return (None, 0)
        #end if

        ptrToNextEle, rest, currentVal = None, None, None
        if cnt > 0:
            currentVal = ptr1.val
            ptrToNextEle, rest = add_rek(ptr1.next, ptr2, cnt - 1)
        else:
            currentVal = ptr1.val + ptr2.val
            ptrToNextEle, rest = add_rek(ptr1.next, ptr2.next, cnt)
        #end if
        newElement = Node(currentVal + rest, ptrToNextEle)
        if newElement.val >= 10:
            newElement.val -= 10
            return (newElement, 1)
        else:
            return (newElement, 0)
        #end if
    #end def
    numberAffterAddition = init_guradian_list()
    numberAffterAddition.next, rest = add_rek(num1.next, num2.next, lenDifference)
    if rest == 1:
        firstElement = Node(1, numberAffterAddition.next)
        numberAffterAddition.next = firstElement
    #end if
    return numberAffterAddition

####################
# helper functions #
####################

def list_to_linked_list(elemList):
    guardian = Node(None, None)
    ptr = guardian
    for ele in elemList:
        ptr.next = Node(ele)
        ptr = ptr.next
    #end for
    return guardian

def init_guradian_list():
    return Node(None, None)

def print_guradian_number(ptr):
    # print("GUARDIAN", end=' -> ')
    while ptr.next != None:
        print(ptr.next.val, end='')
        ptr = ptr.next
    #end while
    print()

if __name__ == "__main__":
    num = [4,2,6,1,5,7,9]
    listNum1 = init_guradian_list()
    listNum1 = list_to_linked_list(num)
    print_guradian_number(listNum1)
   
    num = [1,2,3,4,1]
    listNum2 = None
    listNum2 = list_to_linked_list(num)
    print_guradian_number(listNum2)

    listOfAddedNumbers = add_numbers(listNum1, listNum2)
    print_guradian_number(listOfAddedNumbers)
