def solve():
    n=int(input())
    a=list(map(int,input().split()))
    d = {}
    for item in a:
        i=1
        while(item!=0):
            k = item%2
            item//=2
            if(k!=0):
                if(i in d):
                    d[i]+=1
                else:
                    d[i]=1
            i*=2
    res=0
    for item in d:
        if(d[item]>1):
            res+=item
    print(res)
for _ in range(int(input())):
    solve()