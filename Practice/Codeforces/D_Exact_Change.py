def solve():
    n=int(input())
    a = list(map(int,input().split()))
    a.sort()
    res = 0
    res+=a[-1]//3
    for i in range(len(a)):
        a[i]=a[i]%3
    a.sort()
    res+=a[-1]//2
    for i in range(len(a)):
        a[i]=a[i]%2
    a.sort()
    res+=a[-1]
    print(res)
for _ in range(int(input())):
    solve()