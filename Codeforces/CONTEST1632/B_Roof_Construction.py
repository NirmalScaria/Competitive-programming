import math
def solve():
    n=int(input())
    perfect_power = 2**(math.floor(math.log2(n-1)))
    for i in range(1,n):
        if(i==perfect_power):
            print(0,end=" ")
        print(i,end=" ")
    print()
for _ in range(int(input())):
    solve()