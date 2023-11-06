def panScale(scale, weight, scaleTabIndex, usedScales):
    if weight == 0:
        print(usedScales)
        return True
    if scaleTabIndex == len(scale) or weight < 0:
        return False
    possible = panScale(scale, weight - scale[scaleTabIndex], scaleTabIndex + 1, usedScales + ', ' + str(scale[scaleTabIndex])) or panScale(scale, weight, scaleTabIndex + 1, usedScales) or panScale(scale, weight + scale[scaleTabIndex], scaleTabIndex + 1, usedScales + ', ' + str(scale[scaleTabIndex]))
    return possible

if __name__ == "__main__":
    scale = [1,3,5,10,16,24]
    for weight in range(1,20):
        print(f"weight {weight}:", panScale(scale, weight, 0, ''))