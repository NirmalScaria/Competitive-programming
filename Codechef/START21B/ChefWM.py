import math
def primeFactors(n):
    res=set()
    # Print the number of two's that divide n
    if(n%2==0):
        res.add(2)
    while n % 2 == 0:
        n = n / 2
    # print(res)
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
        
        # while i divides n , print i and divide n
        if(n%i==0):
            res.add(i)
        while n % i== 0:
            n = n / i
    if n > 2:
        res.add(n)
    return(res)



def solve():
    n,m=map(int,input().split())
    k = primeFactors(m)
    if(len(k)==0):
        print(0)
        return
    nfact = len(k)
    for i in range(min((n+1)//2,nfact),0,-1):
        if(n%i==0):
            print(i)
            return
for _ in range(int(input())):
    solve()