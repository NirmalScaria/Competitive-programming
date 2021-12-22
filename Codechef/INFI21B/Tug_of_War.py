def myf(n,m):
    # N is opponent M is me.
    if(n==m):
        print("NO")
        return(0)
    if(m==[]):
        print("NO")
        return(0)
    if(n==[]):
        return([])
    highestval = n[0]
    highestpos = 0
    for i in range(len(n)):
        if(n[i]>highestval):
            highestval=n[i]
            highestpos=i
    if(highestval>m[-1]):
        print("NO")
        return(0)
    if(highestval<m[-1]):
        return(m)
    if(len(m)==1):
        print("NO")
        return(0)
    if(highestpos==len(n)-1):
        return(m[:-2]+[m[-1]]+[m[-2]])
    poppedm = m.pop()
    remainingn = n[:highestpos]+n[highestpos+1:]
    remainingm = m
    recc = myf(remainingn,remainingm)
    if(recc==0):
        return(0)
    ress = recc[:highestpos]+[poppedm]+recc[highestpos:]
    return(ress)
def solve():
    n, m = map(int,input().split())
    n=list(map(int,input().split()))
    m=list(map(int,input().split()))
    m.sort()
    res=myf(n,m)
    if(res!=0):
        print("YES")
        print(" ".join([str(i) for i in res]))
for _ in range(int(input())):
    solve()