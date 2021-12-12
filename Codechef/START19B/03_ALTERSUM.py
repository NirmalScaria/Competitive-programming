t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    cumul = a[:]
    if(len(a)%2 == 0 ):
        cumul[-1]*=-1
    for i in range(len(cumul)-2,-1,-1):
        if(i%2 == 0 ):
            cumul[i]=cumul[i+1]+a[i]
        else:
            cumul[i]=cumul[i+1]-a[i]
    k=min(cumul[:])
    print('alter from ',k)
    finalres=cumul[0]
    print(cumul)
    if(k<0):
        print(finalres-k-k)
    else:
        print(finalres)