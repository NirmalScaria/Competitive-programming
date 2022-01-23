def mexarr(arr):
    kmex, t, res = 0, set(), []
    for i in arr[::-1]:
        t.add(i)
        while(kmex in t):
            kmex+=1
        res+=[kmex]
    res.reverse()
    return(res+[0])

def solve():
    n = int(input())
    a = list(map(int,input().split()))
    mexarray = mexarr(a)
    maxmex = mexarray[0]
    t, kmex, res = set(), 0, [] 
    for i in range(n):
        t.add(a[i])
        while(kmex in t):
            kmex+=1
        if(kmex == maxmex):
            res += [str(kmex)]
            maxmex = mexarray[i+1]
            t, kmex = set(), 0
    print(len(res))
    print(" ".join(res))

for _ in range(int(input())):
    solve()