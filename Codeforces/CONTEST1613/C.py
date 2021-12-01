t=int(input())
for _ in range(t):
    n,h=map(int,input().split())
    arr=list(map(int,input().split()))
    diffs=[]
    for i in range(1,len(arr)):
        diffs+=[arr[i]-arr[i-1]]
    diffs.sort()
    stopp=0
    for i in range(len(diffs)):
        if(diffs[i]*(n-i)>=h):
            res=(h+h%(n-i))//(n-i)
            print(res)
            stopp=1
            break
        h-=diffs[i]
    if(stopp==0):
        print(h)