from random import randint
from math import sqrt

def distance(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def minimal_distatance(T):
    N = len(T)
    subsetCenterLen = 2**N - 1
    subsetCenter = [None for _ in range(subsetCenterLen)]
    subsetCenterIndex = 0

    def gen_subsets(T, index = 0, usedPoints = 0, sumOfCoordinates = (0,0)):
        if index == len(T):
            if usedPoints > 0:
                nonlocal subsetCenterIndex
                nonlocal subsetCenter
                subsetCenter[subsetCenterIndex] = (sumOfCoordinates[0] / usedPoints, sumOfCoordinates[1] / usedPoints)
                subsetCenterIndex += 1
            #end if
            return
        #end if
        gen_subsets(T, index + 1, usedPoints + 1, (sumOfCoordinates[0] + T[index][0], sumOfCoordinates[1] + T[index][1]))
        gen_subsets(T, index + 1, usedPoints, sumOfCoordinates)
    #end def

    gen_subsets(T)
    # print(*subsetCenter, sep='\n')

    minDistance = float('inf')

    for i in range(subsetCenterLen):
        for j in range(i + 1, subsetCenterLen):
            minDistance = min(minDistance, distance(subsetCenter[i], subsetCenter[j]))
        #end for
    #end for

    return minDistance

if __name__ == "__main__":
    points = [(randint(10,100) / randint(1,3), randint(10,100) / randint(1,3)) for _ in range(6)]
    
    print(*points, sep='\n', end="\n\n")
    print(minimal_distatance(points))