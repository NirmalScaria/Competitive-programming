def solve():
    n = int(input())
    k="abc"
    res = []
    for i in range(n//3):
        res+=[k]
    if(n%3==1):
        res+=['a']
    elif(n%3==2):
        res+=['ab']
    print("".join(res))
for _ in range(int(input())):
    solve()