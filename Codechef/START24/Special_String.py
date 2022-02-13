def solve():
    n = int(input())
    s = list(input())
    m = int(input())
    next=[-1]*n
    lasts = [n+1]*27
    for i in range(n-1,-1,-1):
        t=ord(s[i])-ord('a')
        lasts[t]=i
        next[i]=lasts[(t+1)%26]
    best = n+1
    print(next)
    for i in range(n-m+1):
        if(s[i]!='a'):
            continue
        remaining = m
        j=i
        while(remaining>1 and j<=i+best+1):
            j=next[j]
            remaining-=1
        if(remaining<=1):
            best= min(best,j-i+1-m)
            print('best',best,'i',i,'j',j)
        if(best==0):
            break
    if(best>(n-m)):
        print(-1)
    else:
        print(best)
for _ in range(int(input())):
    solve()