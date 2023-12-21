# Zadanie 10. Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać funkcję dodającą
# dwie takie liczby. W wyniku dodawania dwóch liczb powinna powstać nowa lista.

import usefuleFunctions as uf

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
        newElement = uf.Node(currentVal + rest, ptrToNextEle)
        if newElement.val >= 10:
            newElement.val -= 10
            return (newElement, 1)
        else:
            return (newElement, 0)
        #end if
    #end def
    numberAffterAddition = uf.init_guradian_list()
    numberAffterAddition.next, rest = add_rek(num1.next, num2.next, lenDifference)
    if rest == 1:
        numberAffterAddition.next = uf.Node(1, numberAffterAddition.next)
    #end if
    return numberAffterAddition

if __name__ == "__main__":
    num = [4,2,6,1,5,7,9]
    listNum1 = uf.list_to_linked_list(num)
    uf.print_guradian_number(listNum1, myEnd=' + ')
   
    num = [1,2,3,4,1]
    listNum2 = None
    listNum2 = uf.list_to_linked_list(num)
    uf.print_guradian_number(listNum2, myEnd = ' = ')

    listOfAddedNumbers = add_numbers(listNum1, listNum2)
    uf.print_guradian_number(listOfAddedNumbers)


    num = [1,1,1,1,1]
    listNum1 = uf.list_to_linked_list(num)
    uf.print_guradian_number(listNum1, myEnd=' + ')
   
    num = [9,9,9,9,9]
    listNum2 = None
    listNum2 = uf.list_to_linked_list(num)
    uf.print_guradian_number(listNum2, myEnd = ' = ')

    listOfAddedNumbers = add_numbers(listNum1, listNum2)
    uf.print_guradian_number(listOfAddedNumbers)


    num = [1,1,1,1]
    listNum1 = uf.list_to_linked_list(num)
    uf.print_guradian_number(listNum1, myEnd=' + ')
   
    num = [2,2,2,2,2]
    listNum2 = None
    listNum2 = uf.list_to_linked_list(num)
    uf.print_guradian_number(listNum2, myEnd = ' = ')

    listOfAddedNumbers = add_numbers(listNum1, listNum2)
    uf.print_guradian_number(listOfAddedNumbers)
