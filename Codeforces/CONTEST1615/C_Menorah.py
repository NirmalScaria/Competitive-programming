def solve():
    n = int(input())
    a = list(input())
    b = list(input())
    bcount = b.count('1')
    acount = a.count('1')
    aicount = n-acount+1
    if(acount!=bcount and aicount!=bcount):
        print(-1)
        return
    diffcount = 0
    for i in range(len(a)):
        if(a[i]!=b[i]):
            diffcount+=1
    if(acount!=bcount):
        # only ai is possible
        print(n-diffcount)
        return
    if(aicount!=bcount):
        #only a possible
        print(diffcount)
        return
    print(min(diffcount,n-diffcount))
for _ in range(int(input())):
    solve()