from math import isqrt

# increment 1 - if we add -1 - if we subtract
def updateDivsToTab(divs, number, increment):
    assert(number > 1)
    div = 2
    iroot = isqrt(number)
    while div <= iroot:
        while number % div == 0:
            divs[div] += increment
            number //= div
        #end while
        iroot = isqrt(number)
        div += 1
    #end while
    if number > 1:
        divs[number] += increment
    #end if
    return divs

def maxLenWindow(numArray):
    divs = [0 for _ in range(1000)]
    arrayLen = len(numArray)
    myMaxLen = 0
    windowStart, windowEnd = 0, 0
    while windowEnd < arrayLen:
        if max(divs) <= 1:
            divs = updateDivsToTab(divs, numArray[windowEnd], 1)
            windowEnd += 1
        else:
            divs = updateDivsToTab(divs, numArray[windowStart], -1)
            windowStart += 1
        #end if
        if max(divs) <= 1:
            myMaxLen = max(myMaxLen, windowEnd - windowStart)
        #end if
    #end while
    return myMaxLen

def maxLen(numArray):
    arrayLen = len(numArray)
    left, right = 0, 0
    myMaxLen = 0
    divs = [0 for _ in range(1000)]
    while right < arrayLen:
        if max(divs) <= 1:
            currentNumber = numArray[right]
            iroot = isqrt(currentNumber)
            div = 2
            while div <= iroot:
                while currentNumber % div == 0:
                    divs[div] += 1
                    currentNumber //= div
                #end while
                div += 1
                iroot = isqrt(currentNumber)
            #end while
            
            if currentNumber > 1:
                divs[currentNumber] += 1
            #end if
            right += 1
        else:
            currentNumber = numArray[left]
            iroot = isqrt(currentNumber)
            div = 2
            while div <= iroot:
                while currentNumber % div == 0:
                    divs[div] -= 1
                    currentNumber //= div
                #end while
                div += 1
                iroot = isqrt(currentNumber)
            #end while
            
            if currentNumber > 1:
                divs[currentNumber] -= 1
            #end if
            left += 1
        #end if
        if max(divs) <= 1:
            myMaxLen = max(right - left, myMaxLen)
        #end if
    #end while
    return myMaxLen

if __name__ == "__main__":
    numArray = [2,23,33,35,7,4,6,7,5,11,13,22]
    print(maxLen(numArray))
    print(maxLenWindow(numArray))