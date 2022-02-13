def solve():
    n = int(input())
    a = list(map(int, input().split()))
    xors = []
    for i in range(n-1):
        xors += [a[i]^a[i+1]]
    print(xors)

for _ in range(int(input())):
    solve()