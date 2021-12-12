modul=(10**9)+7
t= int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split(" ")))
    d={}
    for item in a:
        if(item in d):
            d[item]+=1
        else:
            d[item]=1
    res=2**len(d)
    for item in d:
        if(d[item]>1):
            res=res+ ( (d[item]-1) * res // 2 )
    res-=1
    print(res%modul)