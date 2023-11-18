def pan_scale(scales, weigth, used, index = 0):
    if weigth == 0:
        print(used)
        return True
    if index == len(scales) or weigth < 0:
        return False
    
    return pan_scale(scales, weigth - scales[index], used + [scales[index]], index + 1) or \
            pan_scale(scales, weigth, used, index + 1) or \
            pan_scale(scales, weigth + scales[index], used + [-scales[index]], index + 1)
            

if __name__ == "__main__":
    scales = [1,2,5,7,11,20]
    for w in range(1, 51):
        possible = ""
        if pan_scale(scales, w, []):
            possible = "possible" 
        else:
            possible = "not possible"
        print(f"weight {w}: {possible}")