def solve():
    n=int(input())
    a = list(map(int,input().split()))
    k = a[:]
    k.sort()
    frags= []
    iswrong = 0
    startind=0
    for i in range(n):
        # print('checking ',a[i],k[i])
        if(a[i]!=k[i]):
            if(iswrong==0):
                
                iswrong=1
                startind = i
                # print('opening at',startind)
        else:
            if(iswrong ==1):
                # print('closing')
                iswrong=0
                frags +=[[startind,i+1]]
    if(iswrong==1):
        frags+=[[startind,n]]
    print(frags)
    if(frags == []):
        print(0)
        return
    prevmin = min(a[frags[0][0]:frags[0][1]])
    prevmax = max(a[frags[0][0]:frags[0][1]])
    if(len(frags)==1):
        print(prevmax - prevmin)
        return
    res = 0
    for i in range(1,len(frags)):
        thismin = min(a[frags[i][0]:frags[i][1]])
        thismax  = max(a[frags[i][0]:frags[i][1]])
        opt1 = prevmax - prevmin + thismax-thismin
        opt2 = max(prevmax,thismax) - min(thismin,prevmin)
        print('options',opt1,opt2)
        if(opt1<opt2):

            res+=opt1
            prevmin = thismin
            prevmax = thismax
        else:
            res+=opt2
            prevmin = min(prevmin,thismin)
            prevmax = max(thismax,prevmax)
    print(res)
for _ in range(int(input())):
    solve()