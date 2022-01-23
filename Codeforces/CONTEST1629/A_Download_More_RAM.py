def solve():
    n , ram = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    k = []
    for i in range(len(a)):
        k+=[[a[i],b[i]]]
    k.sort(key = lambda x:x[0])
    for i in range(len(k)):
        if(k[i][0]>ram):
            print(ram)
            return
        ram+=k[i][1]
    print(ram)
for _ in range(int(input())):
    solve()