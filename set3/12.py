from random import randint

def differenceArithmeticSeries(numArray, arrayLen):
    negativeDifference = 0
    positiveDifference = 0
    maxPositiveSeriesLength = 0
    maxNegativeSeriesLength = 0
    currentNegativeLength = 0
    currentPositiveLength = 0

    for i in range(arrayLen - 1):
        currentDifference = numArray[i + 1] - numArray[i]
        if currentDifference > 0:
            negativeDifference = 0
            currentNegativeLength = 0
            if positiveDifference == 0:
                positiveDifference = currentDifference
                currentPositiveLength += 1
            #end if
            if currentDifference == positiveDifference:
                currentPositiveLength += 1
            else:
                currentPositiveLength = 2
                positiveDifference = currentDifference
            # end if
            maxPositiveSeriesLength = max(maxPositiveSeriesLength, currentPositiveLength)
        elif currentDifference < 0:
            positiveDifference = 0
            currentPositiveLength = 0
            if negativeDifference == 0:
                negativeDifference = currentDifference
                currentNegativeLength += 1
            #end if
            if currentDifference == negativeDifference:
                currentNegativeLength += 1
            else:
                currentNegativeLength = 2
                negativeDifference = currentDifference
            #end if
            maxNegativeSeriesLength = max(maxNegativeSeriesLength, currentNegativeLength)
        else:       #if currentDifferenc == 0:
            positiveDifference = 0
            negativeDifference = 0
            currentPositiveLength = 0
            currentNegativeLength = 0
        #end if
    #end for
    print(f"positive: {maxPositiveSeriesLength}, negative: {maxNegativeSeriesLength}")

    return maxPositiveSeriesLength - maxNegativeSeriesLength


if __name__ == "__main__":
    assert(differenceArithmeticSeries([1,2,3,3,3,4,2,0,1,1,2,3], 12) == 0)
    arrayLen = int(input("enter array length: "))
    numArray = [randint(100, 999) for _ in range(arrayLen)]
    print(numArray)
    print("difference between max arithmetic series length with positive and negative differences:", differenceArithmeticSeries(numArray, arrayLen))
