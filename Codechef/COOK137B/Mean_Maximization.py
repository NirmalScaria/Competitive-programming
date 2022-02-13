def solve():
    n = int(input())
    a = list(map(int,input().split()))
    mx = max(a)
    sm = sum(a)-mx
    res = mx + sm/(n-1)
    print(res)
for _ in range(int(input())):
    solve()