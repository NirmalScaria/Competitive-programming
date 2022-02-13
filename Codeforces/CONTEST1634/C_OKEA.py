def solve():
    n,k=map(int,input().split())
    if(k==1):
        print("YES")
        for i in range(n):
            print(i+1)
        return
    if(n%2==1):
        print("NO")
        return
    print("YES")
    for i in range(n//2):
        added = i*2*k
        for j in range(k):
            print(added+(j*2)+1,end=" ")
        print()
        for j in range(k):
            print(added+(j*2)+2,end=" ")
        print()
for _ in range(int(input())):
    solve()