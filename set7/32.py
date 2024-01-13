# Zadanie 32. Lista reprezentuje wielomian o współczynnikach całkowitych. Elementy w liście ułożone są
# według rosnących potęg. Proszę napisać funkcję obliczającą różnicę dwóch dowolnych wielomianów. 
# Wielomiany reprezentowane są przez wyżej opisane listy. Procedura powinna zwracać wskaźnik do nowo utworzonej
# listy reprezentującej wielomian wynikowy. Listy wejściowe powinny pozostać niezmienione.

import usefuleFunctions as uf

def polynomial_difference(p1, p2):
    newp = uf.Node()
    ptr = newp
    while p1 != None and p2 != None:
        ptr.next = uf.Node(p1.val - p2.val)
        ptr = ptr.next
        p1 = p1.next
        p2 = p2.next
    #end while
        
    # complete polynomial; if list p2 is not empty we have to change factors' signs to opposite 
    # (it's done by multiplying by "m" variable)
    
    m = 1
    if p2 != None:
        p1 = p2
        m = -1
    #end if
        
    while p1 != None:
        ptr.next = uf.Node(m * p1.val)
        ptr = ptr.next
        p1 = p1.next
    #end while

    return newp.next

def print_polynomial(l1):
    pol = ""
    if l1 != None:
        if l1.val != 0:
            pol = f"   {l1.val}"
        #end if
        l1 = l1.next
    #end if
    pow = 1
    while l1 != None:
        factor = l1.val
        sign = ' + ' if factor > 0 else ' - '
        factor = abs(factor)
        if factor != 0:
            pol += sign
            # pol += f" {sign} {factor}x^{pow}"
            if factor != 1:
                pol += str(factor)
            #end if
            pol += f"x^{pow}"
        pow += 1
        l1 = l1.next
    #end while
    print(pol[3:])

if __name__ == "__main__":
    tab = [1,0,0,0,-3]          # 1 * x^0 + 0 * x^1 + 0 * x^2 + 0 * x^3 + -3 * x^4
    l1 = uf.remove_guradian(uf.list_to_linked_list(tab))
    tab = [2,1,1,1,-7,-1,-1,-1]
    l2 = uf.remove_guradian(uf.list_to_linked_list(tab))
    uf.print_list(l1)
    print_polynomial(l1)
    print_polynomial(l2)
    # uf.print_list(l2)
    newPol = polynomial_difference(l1, l2)
    # uf.print_list(newPol)
    print_polynomial(newPol)
