t=int(input())
def isprime(x):
    for i in range(2,int(x**1/2)+1):
        if(x%i==0):
            return(0)
    return(1)
for _ in range(t):
    n,e=map(int,input().split())
    arr=list(map(int,input().split()))
    isprimes=[isprime(l) for l in arr]
    count=0
    for i in range(n-1):
        fl=0
        if(isprimes[i]):
            if(arr[i]!=1):
                fl+=1
            t=i+e
            while(t<n and isprimes[t] and fl<2):
                if(arr[t]!=1):
                    fl+=1
                if(fl==1):
                    # print(arr[i],' to ',arr[t])
                    count+=1
                t+=e
    print(count)