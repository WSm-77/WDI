from random import randint

##################
# first solution #
##################

def maxAscendingSeq(tab, numberOfElements):
    maxAscending = 1
    currentAscending = 1
    for i in range(numberOfElements - 1):
        if tab[i + 1] > tab[i]:
            currentAscending += 1
            maxAscending = max(maxAscending, currentAscending)
        else:
            currentAscending = 1
        #end if
    #end for
    return maxAscending

###################
# second solution #
###################

def maxAscendingVersion2(tab, numberOfElements):
    maxAscending = 1
    currentAscending = 1
    firstNumberInMaxSeq = tab[0]
    firstNumberInCurrentSeq = tab[0]
    for i in range(numberOfElements - 1):
        if tab[i + 1] > tab[i]:
            currentAscending += 1
        else:
            if currentAscending > maxAscending:
                firstNumberInMaxSeq = firstNumberInCurrentSeq
                maxAscending = currentAscending
            #end if
            currentAscending = 1
            firstNumberInCurrentSeq = tab[i + 1]
        #end if
    else:
        currentAscending -= 1
        if currentAscending > maxAscending:
            firstNumberInMaxSeq = firstNumberInCurrentSeq
            maxAscending = currentAscending
        #end if
    #end for
    return maxAscending, firstNumberInMaxSeq

if __name__ == "__main__":
    numberOfElements = int(input("enter number of elements in tab: "))
    tab = [randint(1, 1000) for _ in range(numberOfElements)]
    print(tab)
    print("max ascending sequence:", maxAscendingSeq(tab, numberOfElements))
    myTuple = maxAscendingVersion2(tab, numberOfElements)
    print(f"max ascending seqence: {myTuple[0]}, starts from: {myTuple[1]}")