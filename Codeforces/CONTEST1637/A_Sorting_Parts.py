def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b= a[:]
    a.sort()
    if(b!=a):
        print("YES")
    else:
        print("NO")
for _ in range(int(input())):
    solve()