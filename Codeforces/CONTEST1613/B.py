t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    res=[]
    minn=min(arr)
    i=0
    while(len(res)<len(arr)//2):
        if(arr[i]==minn):
            i+=1
            continue
        res+=[str(arr[i])+" "+str(minn)]
        i+=1
    print("\n".join(res))