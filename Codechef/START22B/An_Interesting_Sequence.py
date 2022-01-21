import math
def solve():
    k = int(input())
    if(k%2==1):
        print(0)
        return
    for i in range(50):
        if(k%(2**i)!=0):
            print(i-1)
            return
for _ in range(int(input())):
    solve()