def solve():
    n, a = map(int,input().split())
    if(a%2==1):
        if(n%2==0):
            print("Even")
        else:
            print("Odd")
        return
    if(n==1):
        print("Even")
    else:
        print("Impossible")
    return
for _ in range(int(input())):
    solve()