def solve():
    n = int(input())
    res = [1]
    p=0
    while(len(res)<n):
        p+=1
        res=res+[2**p]+res
    print(*res[:n])
for _ in range(int(input())):
    solve()