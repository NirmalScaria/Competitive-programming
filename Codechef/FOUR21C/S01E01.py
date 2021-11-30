t=int(input())
for _ in range(t):
    n,x,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    similars=0
    for i in range(len(a)):
        if(abs(a[i]-b[i])<=k):
            similars+=1
    if(similars>=x):
        print("YES")
    else:
        print("NO")