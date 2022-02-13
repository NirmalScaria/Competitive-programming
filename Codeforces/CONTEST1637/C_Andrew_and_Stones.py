import math
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if(n==3):
        if(a[1]%2==1):
            print(-1)
            return
    insideCount = a[1:-1].count(1)
    if(insideCount==n-2):
        print("-1")
        return
    res = 0
    for item in a[1:-1]:
        res += math.ceil(item/2)
    print(res)
for _ in range(int(input())):
    solve()