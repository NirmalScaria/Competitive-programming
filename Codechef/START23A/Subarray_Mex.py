def solve():
    n,k,x = map(int,input().split())
    if(k<x):
        print(-1)
        return
    t=0
    for _ in range(n):
        print(t,end=" ")
        t=(t+1)%x
    print()
for _ in range(int(input())):
    solve()