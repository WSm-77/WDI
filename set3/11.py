from random import randint

def longestGeometricSeq(numArray, arrayLen):
    assert(arrayLen > 1)
    curretnGeometricSeqLength = maxGeometricSeqLength = 2
    seqQotient = round(numArray[1] / numArray[0], 7)
    # print("seqQotient:", seqQotient)
    for i in range(1, arrayLen - 1):
        currentQotient = round(numArray[i + 1] / numArray[i], 7)
        # print("current Qotionet:", currentQotient)
        if currentQotient == seqQotient:
            curretnGeometricSeqLength += 1
            maxGeometricSeqLength = max(maxGeometricSeqLength, curretnGeometricSeqLength)
        else:
            seqQotient = currentQotient
            maxGeometricSeqLength = 2
        #end if
    #end for
    return maxGeometricSeqLength

if __name__ == "__main__":
    arrayLen = int(input("enter array length: "))
    numArray = [randint(1,100) for _ in range(arrayLen)]
    print(numArray)
    assert((longestGeometricSeq([2,6,18], 3) == 3))
    assert((longestGeometricSeq([18,6,2], 3) == 3))
    assert((longestGeometricSeq([343,49,7,1], 4) == 4))
    print(longestGeometricSeq(numArray, arrayLen))