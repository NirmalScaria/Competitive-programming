def solve():
    n,x,y = map(int,input().split())
    c = ((n+1)//2)
    dist = abs(x-c) + abs(y-c)
    if(dist%2)==0:
        print(0)
    else:
        print(1)
for _ in range(int(input())):
    solve()