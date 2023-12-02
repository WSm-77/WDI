def in_parrarel(res1, res2):
    return (res1 * res2) / (res1 + res2)

def in_series(res1, res2):
    return res1 + res2

def resistance(T, targetResistance, index = 0, currentResistance = 0, numberOfUsedRestistors = 0):
    if numberOfUsedRestistors == 3:
        if currentResistance == targetResistance:
            return True
        else:
            return False
        #end if
    #end if

    if index == len(T):
        return False
    #end if

    if  resistance(T, targetResistance, index + 1, in_series(currentResistance, T[index]), numberOfUsedRestistors + 1) or \
        resistance(T, targetResistance, index + 1, currentResistance, numberOfUsedRestistors):
            return True
    #end if

    if currentResistance != 0 and resistance(T, targetResistance, index + 1, in_parrarel(currentResistance, T[index]), numberOfUsedRestistors + 1):
            return True
    #end if

    return False

if __name__ == "__main__":
    resistors = [1,8,6,9,3,2,5,7]

    for targetRes in range(50):
        print(f"resisitance {targetRes + 1}: {resistance(resistors, targetRes + 1)}")