t=int(input())
for _ in range(t): 
    n,m=map(int,input().split())
    orv=0
    res=0
    powv=pow(2,n-1)
    k=1
    for _ in range(m):
        l,r,x=map(int,input().split())
        orv=orv|x
    res=pow(2,n-1)*orv
    res=res%(pow(10,9)-7)
    print(res)