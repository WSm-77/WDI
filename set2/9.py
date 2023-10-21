def f(x):
    assert(x != 0)

    return 1/x

def calculateArea(x1, x2, numberOfRectangles):
    area = 0
    a = (x2 - x1) / numberOfRectangles
    center = x1 + (a / 2)
    for i in range(numberOfRectangles):
        b = f(center)
        center += a
        area += a * b
    #end for
    return area



if __name__ == "__main__":
    print(calculateArea(1, 10, 1000))