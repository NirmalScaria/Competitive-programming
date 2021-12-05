def remainingH(arr,midl,th):
    for i in range(len(arr)-1):
        th-=min(midl,(arr[i+1]-arr[i]))
        if(th<=0):
            return(True)
    th-=midl
    return(th<=0)

t=int(input())
for _ in range(t):
    n,h=map(int,input().split())
    arr=list(map(int,input().split()))
    l=1
    r=int(1e18)
    ans=int(1e18)
    while(l<=r):
        mid=(l+r)//2
        if(remainingH(arr,mid,h)):
            ans=min(ans,mid)
            r=mid-1
        else:
            l=mid+1
    print(ans)