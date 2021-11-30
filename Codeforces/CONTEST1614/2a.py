t = int(input())
for _ in range(t):
    n=int(input())
    visits=list(map(int,input().split()))
    visits=[[i,visits[i]] for i in range(len(visits))]
    visits.sort(key=lambda x:x[1],reverse=True)
    dist=0
    res=[0 for _ in range(n+1)]
    away=1
    for i in range(0,n,2):
        res[visits[i][0]+1]=away
        dist+=visits[i][1]*2*away
        if(i<n-1):
            res[visits[i+1][0]+1]=0-away
            dist+=visits[i+1][1]*2*away
        away+=1
    print(dist)
    print(' '.join([str(i) for i in res]))