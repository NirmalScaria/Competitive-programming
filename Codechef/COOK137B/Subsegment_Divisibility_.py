def solve():
    n = int(input())
    for i in range(1,n//2+1):
        print(i*2+1,i*2,end=" ")
    if(n%2==1):
        print(n+2,end="")
    print()
for _ in range(int(input())):
    solve()