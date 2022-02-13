def isprime(n):
    i=2
    while(i*i<=n):
        if(n%i==0):
            return(0)
        i+=1
    return(1)
def solve():
    n = int(input())
    i=n-1
    while(i>=2):
        if(isprime(i)==1):
            if(n%2==1):
                print(((n-1)*i)//2+1)
                return
            else:
                print((n*i)//2)
                return
        i-=1
for _ in range(int(input())):
    solve()