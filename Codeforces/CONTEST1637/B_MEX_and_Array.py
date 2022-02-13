def solve():
    n=int(input())
    a=list(map(int,input().split()))
    res = 0
    for i in range(1,n+1):
        for j in range(n-i+1):
            res+=(a[j:j+i]).count(0) + i
    print(res)
for _ in range(int(input())):
    solve()