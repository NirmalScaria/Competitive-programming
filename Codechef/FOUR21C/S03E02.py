def calcflips(s,t,i):
    flips=0
    for i in range(len(s)-1):
        if(s[i]!=t[i]):
            s[i]=t[i]
            s[i+1]=0 if s[i+1]==1 else 1
            flips+=1
    if(s[-1]!=t[len(s)-1]):
        flips+=1
    flips+=lt-ls
    return(flips)

t=int(input())
for _ in range(t):
    ls,lt=map(int,input().split())
    s=[int(i) for i in input()]
    t=[int(i) for i in input()]
    if(ls>lt):
        print(-1)
    elif(ls==lt and s.count(1)%2!=t.count(1)%2):
        print(-1)
    else:
        flips=0
        for i in range(len(s)-1):
            if(s[i]!=t[i]):
                s[i]=t[i]
                s[i+1]=0 if s[i+1]==1 else 1
                flips+=1
        if(s[-1]!=t[len(s)-1]):
            flips+=1
        flips+=lt-ls
        print(flips)