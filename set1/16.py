LIM = 1

def stepsToOne(a):
    stepsCounter = 0
    while LIM != a:
        stepsCounter += 1
        a = (a % 2)*(3 * a + 1)+(1 - (a % 2))*(a // 2)
        # print(a)
    # print(stepsCounter)
    return stepsCounter

def maxSteps():
    max = 0
    number = 0
    for i in range(2, 10000 + 1):
        a = stepsToOne(i)
        if a > max:
            max = a
            number = i
    print("number:", number)
    return max

if __name__ == '__main__':
    print("liczba kroków:", maxSteps())