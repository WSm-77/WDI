def calc_mass_center(sumOfCoordinates, numberOfCoordinates):
    assert(numberOfCoordinates != 0)
    return (sumOfCoordinates[0] / numberOfCoordinates, sumOfCoordinates[1] / numberOfCoordinates)

def distance(R, point):
    return point[0]**2 + point[1]**2 < R**2

def is_possible(T, R , k, index = 0, sumOfCoordinates = (0, 0), numberOfUsedCoordinates = 0, usedPoints = []):
    if numberOfUsedCoordinates >= k:
        return False
    
    if 0 < numberOfUsedCoordinates and numberOfUsedCoordinates % 3 == 0 and distance(R, calc_mass_center(sumOfCoordinates, numberOfUsedCoordinates)):
        print(usedPoints)
        return True
    
    if index == len(T):
        return False
    
    if is_possible(T, R, k, index + 1, (sumOfCoordinates[0] + T[index][0], sumOfCoordinates[1] + T[index][1]), numberOfUsedCoordinates + 1, usedPoints + [T[index]]) or \
       is_possible(T, R, k, index + 1, sumOfCoordinates, numberOfUsedCoordinates, usedPoints):
        return True
    
    return False

if __name__ == "__main__":
    tab = [(-1, 0), (17, 45), (2, 5), (42, 5), (-4, 8), (1, 4), (-3, -3), (2, 0)]
    R = 0.1
    k = 7

    print(is_possible(tab, R, k))

    tab = [(-1, 2), (17, 45), (20, 5), (42, 5), (-4, 8), (5, 4), (-3, -3)]
    R = 2
    k = 7

    print(is_possible(tab, R, k))