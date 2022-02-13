def solve():
    n = int(input())
    a = list(map(int,input().split()))
    best,d = n, {}
    for i in range(n):
        if a[i] in d: best = min(best,i-d[a[i]])
        d[a[i]] = i
    print(-1 if best>=n else n-best)
for _ in range(int(input())):
    solve()