def solve():
    n = int(input())
    if(n==2):
        print("NO")
        return
    print("YES")
    if(n%2==1):
        for i in range(1,n//2+1):
            print(i,end=" ")
        for i in range(n,n//2,-1):
            print(i,end=" ")
    else:
        print(n//2, end=" ")
        for i in range(1,n//2):
            print(i,end=" ")
        for i in range(n,n//2,-1):
            print(i,end=" ")
    print()
for _ in range(int(input())):
    solve()