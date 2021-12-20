import math
def solve():
    count=0
    n = int(input())
    if(n==1):
        print(1)
        return
    res = int(math.sqrt(n))
    if(n**(1/2) != int(n**(1/2)) and math.ceil(n**(1/2))**2 == n):
        res+=1
    res += int(n**(1/3))
    if(n**(1/3) != int(n**(1/3)) and math.ceil(n**(1/3))**3 == n):
        res+=1
    res -= int(n**(1/6))
    if(n**(1/6) != int(n**(1/6)) and math.ceil(n**(1/6))**6 == n):
        res-=1
    print(res)
for _ in range(int(input())):
    solve()