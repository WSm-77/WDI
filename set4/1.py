##################
# first solution #
##################

def fillTableSpiraly(tab):
    tabLen = len(tab)
    cntr = 1
    firstEdge = 0
    secondEdge = tabLen - 1
    while secondEdge >= firstEdge:
        for i in range(firstEdge, secondEdge + 1):
            tab[firstEdge][i] = cntr
            cntr += 1
        #end for
        for j in range(firstEdge + 1, secondEdge):
            tab[j][secondEdge] = cntr 
            cntr += 1
        #end for
        for k in range(secondEdge, firstEdge, -1):
            tab[secondEdge][k] = cntr 
            cntr += 1
        #end for
        for l in range(secondEdge, firstEdge, -1):
            tab[l][firstEdge] = cntr
            cntr += 1
        #end for
        firstEdge += 1
        secondEdge -= 1
    #end while
    print(*tab, sep="\n", end='\n\n')

###################
# second solution #
###################

def fillTableRecursively(tab):
    tabLen = len(tab)
    assert(tabLen >= 0)
    def fillRecursively(tab, tabSize, tabStart, number):
        if tabSize == 0:
           return
         #end if
        if tabSize == 1:
            tab[tabStart][tabStart] = number
            return
        #end if
        tabEdge = tabStart + tabSize - 1
        for i in range(tabStart, tabEdge):
           tab[tabStart][i] = number
           number += 1
        #end for
        for j in range(tabStart, tabEdge):
            tab[j][tabEdge] = number
            number += 1
        #end for
        for k in range(tabEdge, tabStart, -1):
            tab[tabEdge][k] = number
            number += 1
        #end for
        for l in range(tabEdge, tabStart, -1):
            tab[l][tabStart] = number
            number += 1
        #end for
        fillRecursively(tab, tabSize - 2, tabStart + 1, number)
    fillRecursively(tab, tabLen, 0, 1)
    print(*tab, sep="\n")

if __name__ == "__main__":
    n = 7
    tab = [[0 for _ in range(n)] for _ in range(n)]
    tab2 = [[0 for _ in range(n)] for _ in range(n)]
    fillTableSpiraly(tab)
    fillTableRecursively(tab2)