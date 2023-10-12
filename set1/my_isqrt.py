def main():
    n = int(input("enter number: "))
    sum = 0
    an = 1
    isqrt = -1
    while sum<=n:
        sum += an
        isqrt += 1
        an += 2
    print(isqrt)
    

main()