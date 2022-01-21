def solve():
    n,m = map(int,input().split())
    res = []
    for i in range(n):
        for j in range(m):
            dist = max(i+j , m+n-i-j-2)
            dist = max(dist, m-j+i-1)
            dist = max(dist, n-i+j-1)
            res+=[dist]
    res.sort()
    print(" ".join([str(i) for i in res]))

for _ in range(int(input())):
    solve()