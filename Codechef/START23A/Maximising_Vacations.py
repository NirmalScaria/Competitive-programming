def solve():
    n, x = map(int,input().split())
    s = list(input().split('1'))
    res = 0
    if(len(s)==1):
        print(n//x)
        return
    added = 0
    for i in range(len(s)-1):
        res += len(s[i])//x
        if((len(s[i])+len(s[i+1])+1)//x > (len(s[i])//x+len(s[i+1])//x) and added==0):
            res+=1
            added=1
    res+=len(s[-1])//x
    print(res)
for _ in range(int(input())):
    solve()