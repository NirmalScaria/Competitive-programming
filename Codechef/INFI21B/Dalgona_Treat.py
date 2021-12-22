import math
def solve():
    n = int(input())
    if(n==2):
        print(2)
        print(3,1)
        print(4,1)
        return
    if(n==4):
        print(1)
        print(1,4)
        return
    if(n==1):
        print(1)
        print(1,1)
        return
    if(n%2==0):
        print(2)
        print(n//2-1,1)
        print(1,n-1) 
    else:
        print(2)
        print(2,n-1)
        print(n-2,1)

for _ in range(int(input())):
    solve()