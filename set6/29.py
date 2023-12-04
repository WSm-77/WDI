from random import randint

def valid_distance(r, point):
    return point[0]**2 + point[1]**2 + point[2]**2 <= r**2

def center_of_mass(T, r):
    found = False
    def rek(T, r, index = 0, usedPoints = [], sumOfMasses = (0,0,0), numberOfUsedPoints = 0):

        nonlocal found
        if numberOfUsedPoints >= 3:
            centerOfMass = (sumOfMasses[0] / numberOfUsedPoints, \
                                      sumOfMasses[1] / numberOfUsedPoints, \
                                      sumOfMasses[2] / numberOfUsedPoints)    # we don't divide by 0, cuz sumOfMasses >= 3
            if valid_distance(r, centerOfMass):
                found = True
                print(*usedPoints, sep="\n")
                print("center of mass:", centerOfMass, "distance:", (centerOfMass[0]**2 + centerOfMass[1]**2 + centerOfMass[2]**2)**0.5)
                return
        #end if

        if index == len(T):
            return
        #end if

        currentPoint = T[index]
        rek(T, r, index + 1, usedPoints + [currentPoint], (sumOfMasses[0] + currentPoint[0], sumOfMasses[1] + currentPoint[1], sumOfMasses[2] + currentPoint[2]), numberOfUsedPoints + 1)

        if not found:
            rek(T, r, index + 1, usedPoints, sumOfMasses, numberOfUsedPoints)
        #end if

    #end def
    rek(T, r)

    return found
            
if __name__ == "__main__":
    tab = [(-1, 0, -2), (17, 45, 20), (2, 4, 6), (42, 5, 18), (-4, 8, -2)]
    r = 5
    print(*tab)
    print("r =", r, "\b:", center_of_mass(tab, r))

    tab = [(randint(0, 20), randint(-20, 20), randint(0, 20)) for _ in range(15)]
    print(*tab, sep="\n")
    for r in range(1, 10 + 1):
        print("r =", r, "\b:", center_of_mass(tab, r), end="\n\n")


