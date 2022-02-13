def solve():
    n,x,y = map(int,input().split())
    a=list(map(int,input().split()))
    s = sum(a)
    if(y%2==x%2):
        if(s%2==0):
            print('Alice')
            return
        else:
            print('Bob')
            return
    else:
        if(s%2==0):
            print('Bob')
            return
        else:
            print('Alice')
            return
for _ in range(int(input())):
    solve()