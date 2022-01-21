def solve():
    n,m,r,c = map(int,input().split())
    a=[]
    for i in range(n):
        a+=[list(input())]
    r-=1
    c-=1
    if(a[r][c]=='B'):
        print(0)
        return
    for i in range(m):
        if(a[r][i]=='B'):
            print(1)
            return
    for i in range(n):
        if(a[i][c]=='B'):
            print(1)
            return
    for i in range(n):
        for j in range(m):
            if(a[i][j]=='B'):
                print(2)
                return
    print(-1)
    return
for _ in range(int(input())):
    solve()