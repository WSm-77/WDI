FI=1.618

def main():
    # n=int(input("n: "))
    # printFirstFibNum(n)
    # printNFibNumbers(n)
    printTraditionalFib(32,17,10000)

#function that returns first 2 numbers of Fibonacci sequence in which "n" is one of the numbers in this sequence
def printFirstFibNum(n):

    #previous number in Fibonacci seqence
    prev=round(n/FI)

    while prev>=0:
        # print(n)
        pom=n-prev
        n=prev
        prev=pom
    print(n, n+prev)

#function that prints "n" first numbers of Fibonacci sequence
def printNFibNumbers(n):
    fib=17
    while True:
        print(fib)
        fib=round(fib*FI)
        if fib>n:
            break

def printTraditionalFib(first,second,stop):
    while first<=stop:
        print(first)
        second+=first
        first=second-first
    
main()