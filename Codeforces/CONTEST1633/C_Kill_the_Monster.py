def solve():
    hc,dc = map(int,input().split())
    hm,dm = map(int,input().split())
    k,w,a = map(int,input().split())
    for i in range(k+1):
        wpn = dc + w*i
        hlt = hc + a*(k-i)
        if((hlt-1)//dm >= (hm-1)//wpn):
            print("YES")
            return
    print("NO")
for _ in range(int(input())):
    solve()