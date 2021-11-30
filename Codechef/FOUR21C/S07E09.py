t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    smallest=a[0]
    for item in a:
        smallest=min(item,smallest)
    sn=0
    for item in a:
        if(item==smallest):
            sn+=1
    res=(smallest+1)*n-sn
    print(res)