def solve():
    n,k=map(int,input().split())
    a=list(input())
    count=0
    for i in range((n+1)//2):
        if(a[i]!=a[n-1-i]):
            count+=1
    if(count>k):
        print("NO")
        return
    if(n%2==1):
        print("YES")
        return
    if((k-count)%2==0):
        print("YES")
    else:
        print("NO")
for _ in range(int(input())):
    solve()