t=int(input())
for _ in range(t):
    n=int(input())
    visits = list(map(int,input().split()))
    d={}
    for i in range(n):
        d[i]=visits[i]
    d={k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
    res=[]
    mindist=0
    lr=-1
    res+=[1]
    presdest=0
    for key,val in d.items():
        if(lr==-1):
            presdest+=1
            res=[key+2]+res
        else:
            res=res+[key+2]
        mindist+=2*val*presdest
        lr*=-1
    actres=[0 for _ in range(n+1)]
    for i in range(len(res)):
        actres[res[i]-1]=i+1
    
    print(mindist)
    print(" ".join([str(i) for i in actres]))