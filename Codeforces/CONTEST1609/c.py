t=int(input())
def isprime(x):
    for i in range(2,int(x**1/2)+1):
        if(x%i==0):
            return(0)
    return(1)
for _ in range(t):
    n,e=map(int,input().split())
    arr=list(map(int,input().split()))
    visited = [0 for _ in range(n)]
    count=0
    for p in range(e):
        print('start from ',arr[p])
        i=p
        while(i<n):
            # print('cluster ended')
            if(arr[i]==1):
                tmpcnt=0
                itmp=i
                while(i<n and arr[i]==1):
                    i+=e
                    tmpcnt+=1
                if(i<n and isprime(arr[i])):
                    count+=tmpcnt
                    print(tmpcnt, '1s before ',arr[i])
                if(itmp>=e and isprime(arr[itmp-e])):
                    #  ones crossing a prime to be implemented.
                    # afi=itmp-e
                    # aftercount=0
                    # while(afi>=e and arr[afi-e]==1):
                    #     aftercount+=1
                    #     afi-=e
                    count+=tmpcnt
                    print(tmpcnt,'1s after',arr[itmp-e])
            i+=e
    print(count)