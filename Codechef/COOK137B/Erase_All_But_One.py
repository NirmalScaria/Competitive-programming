def solve():
    n = int(input())
    p = list(map(int,input().split()))
    mx = []
    for item in p[::-1]:
        mx +=[max()]
    for i in range(len(p)):
        mx = max(p)
        if(p[i]==mx):
            print("NO")
            return
        if(p[i]<p[-1]):
            print("YES")
            return
        
for _ in range(int(input())):
    solve()