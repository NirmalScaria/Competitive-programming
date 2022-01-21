def solve():
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    mx = (a[-1]-a[0]) * a[-2]
    mx = max(mx, ((a[-2]-a[0])*a[-1]))
    print(mx)
for _ in range(int(input())):
    solve()