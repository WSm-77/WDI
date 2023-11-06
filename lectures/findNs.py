cntr = 0

def findNs(tab, n, targetProduct, elementIndex = 0):
    global cntr
    if n == 1:
        for i in range(elementIndex, len(tab)):
            if tab[i] == targetProduct:
                cntr +=1
    else:
        for i in range(elementIndex, len(tab)):
            if targetProduct % tab[i] == 0:
                findNs(tab, n - 1, targetProduct//tab[i], i + 1)



if __name__ == "__main__":
    tab = [7,12,7,15,12,2,3,2,3,4,7,45,4,9,10,5]
    targetProduct = 180
    n = 3
    findNs(tab, n, targetProduct)
    print(cntr)