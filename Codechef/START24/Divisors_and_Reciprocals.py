import math
def solve():
    x,a,b = map(int,input().split())
    if(x%a !=0 or a<b):
        print(-1)
        return
    if(a<=b):
        if(a==b and x==1):
            print(1)
            return
        else:
            print(-1)
            return
    n = (x*b)//a
    print(n)
for _ in range(int(input())):
    solve()