
vals = [100000 for _ in range(1003)]
vals[0]=0
vals[1]=0
for i in range(1003):
    for j in range(i+1,0,-1):
        possible = i + i//j
        if(possible<1003):
            vals[possible] = min(vals[possible],vals[i]+1)
        else:
            break
def solve():
    n,k = map(int,input().split())
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    toadd = [0 for _ in range(len(b))]
    for i in range(len(b)):
        toadd[i]=vals[b[i]]
    res=0
    for i in range(len(c)):
        if(toadd[i]==0):
            res+=c[i]
            c[i]=0
    res += knapSack(k,toadd,c,n)
    # print(toadd)
    print(res)
for _ in range(int(input())):
    solve()