def solve():
    n = int(input())
    a= list(map(int,input().split()))
    if(sum(a)%n==0):
        print(0)
    else:
        print(1)
for _ in range(int(input())):
    solve()