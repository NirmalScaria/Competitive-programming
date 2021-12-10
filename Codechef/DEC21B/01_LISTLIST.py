t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if(len(a)<2):
        print(0)
        continue
    d={}
    for i in range(len(a)):
        if(a[i] in d):
            d[a[i]]+=1
        else:
            d[a[i]]=1
    highcount=1
    for item in d:
        if(d[item]>highcount):
            highcount=d[item]
    if( highcount==1 and n>1 ):
        print(-1)
    elif(highcount==n):
        print(0)
    else:
        print(n-highcount+1)