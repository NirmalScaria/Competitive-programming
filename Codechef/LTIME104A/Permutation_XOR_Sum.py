import math
def ans(n):
    if(n<=1):
        return(0)
    highestpower = math.floor(math.log2(n))
    count = min(n - 2**highestpower +1, 2**highestpower -1)
    val = 2**(highestpower+1) -1
    print('pwoer',2**highestpower,'count:',count,'val:',val)
def solve():
    n = int(input())
    if(n==1):
        print(0)
        return
    print('input:',n)
    res = ans(n)
for _ in range(int(input())):
    solve()