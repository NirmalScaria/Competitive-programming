import math
def solve():
    n=int(input())
    a=list(map(int,input().split()))
    x=1
    b=0
    b=0
    target = a[-1]
    i=n-2
    while(i>=0):
        if(target==a[i]):
            x+=1
        else:
            b+=1
            i-=x
            x*=2
            i+=1
        i-=1
    print(b)
for _ in range(int(input())):
    solve()