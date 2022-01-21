def grayCode(n):
    return n ^ (n >> 1)

def solve():
    n = int(input())
    for i in range(1,n+1):
        print(grayCode(i*2), end=" ")
    print()
for _ in range(int(input())):
    solve()