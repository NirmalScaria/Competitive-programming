t=int(input())
for _ in range(t):
    n,k=input().split()
    n=list(int(n[i]) for i in range(len(n)))
    k=int(k)
    n.sort()
    while(k>0):
        if(n[0]==9):
            break
        n[0]+=1
        i=1
        while(i<len(n) and n[0]>n[i]):
            i+=1
        i-=1
        t=n[0]
        n[0]=n[i]
        n[i]=t
        k-=1
    res=1
    for item in n:
        res*=item
    print(res)