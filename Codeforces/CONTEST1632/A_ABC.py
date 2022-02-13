def solve():
    n = int(input())
    a = list(input())
    if(n<=1):
        print("YES")
        return()
    if(n<=2):
        if(a[0]!=a[1]):
            print("YES")
            return()
    print("NO")
for _ in range(int(input())):
    solve()