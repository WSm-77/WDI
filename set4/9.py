def isProductEqualK(tab, rowStart, collStart, squareLen, k):
    topLeft = tab[rowStart][collStart]
    topRight = tab[rowStart][collStart + squareLen]
    botLeft = tab[rowStart + squareLen][collStart]
    botRight = tab[rowStart + squareLen][collStart + squareLen]
    return topLeft * topRight * botLeft * botRight == k

# k - target product
def squareWithProductK(tab, k):
    tabLen = len(tab)
    doesSquareExist = False
    squareCenterRow = 0
    squareCenterColl = 0
    if tabLen % 2 == 0:
        squareLen = tabLen - 2
    else:
        squareLen = tabLen - 1
    #end if

    while squareLen > 0:
        for rowStart in range(tabLen - squareLen):
            for collStart in range(tabLen - squareLen):
                if isProductEqualK(tab, rowStart, collStart, squareLen, k):
                    doesSquareExist = True
                    distanceToCenter = squareLen // 2
                    squareCenterRow = rowStart + distanceToCenter
                    squareCenterColl = collStart + distanceToCenter
                    break
                #end if
            #end for
            if doesSquareExist:
                break
            #end if
        #end for
        squareLen -= 2
    #end while
    if doesSquareExist:
        print(f"squareCenter = ({squareCenterRow},{squareCenterColl})")
    else:
        print("not found")

if __name__ == "__main__":
    k = 54      # center = (2,1)
    tab = [[1,81,3,4,5],
           [1,4,27,5,5],
           [1,1,1,9,7],
           [1,5,2,4,3],
           [1,1,1,1,1]]
    
    squareWithProductK(tab, k)

    k = 5       # center = (2,2)
    
    squareWithProductK(tab, k)

    k = 2916       # center = (1,2)
    
    squareWithProductK(tab, k)

    k = 2       # doesn't exist
    
    squareWithProductK(tab, k)