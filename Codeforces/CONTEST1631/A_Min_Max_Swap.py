def solve():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(len(a)):
        if(a[i]<b[i]):
            temp=a[i]
            a[i]=b[i]
            b[i]=temp
    print(max(a)*max(b))
for _ in range(int(input())):
    solve()