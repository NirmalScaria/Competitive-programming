def solve():
    n,k = map(int,input().split())
    s = list(input())
    r = s[:]
    r.reverse()
    if(s==r):
        print(1)
        return
    if(k==0):
        print(1)
        return
    print(2)
    return
for _ in range(int(input())):
    solve()