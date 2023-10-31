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
    print(*tab, sep="\n")

if __name__ == "__main__":
    n = 7
    tab = [[0 for _ in range(n)] for _ in range(n)]
    fillTableSpiraly(tab)