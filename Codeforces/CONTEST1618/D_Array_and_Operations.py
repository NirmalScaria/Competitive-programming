t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    res=0
    for i in range(n-1,n-k-1,-1):
        print(a[i])
        print('i is',i)
    print('done')