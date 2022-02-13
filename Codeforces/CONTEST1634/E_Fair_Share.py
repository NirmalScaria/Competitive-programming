
def solve():
    n = int(input())
    a=[]
    for i in range(n):
        d = int(input())
        a+=[list(map(int,input().split()))]
    ans=[]
    l={}
    r={}
    sizel=sizer=0
    for item in a:
        ans+=[[]]
        for i in item:
            if(i not in l and i not in r):
                if(sizel<sizer):
                    l[i]=1
                    sizel+=1
                    ans[-1]+=['L']
                else:
                    r[i]=1
                    sizer+=1
                    ans[-1]+=['R']
            elif(i in l and i in r):
                if(l[i]>r[i]):
                    r[i]+=1
                    sizer+=1
                    ans[-1]+=['R']
                else:
                    l[i]+=1
                    sizel+=1
                    ans[-1]+=['L']
            elif(i in l):
                r[i]=1
                sizer+=1
                ans[-1]+=['R']
            else:
                l[i]=1
                sizel+=1
                ans[-1]+=['L']
    for i in l:
        if i not in r:
            print("NO")
            return
        if(l[i]!=r[i]):
            print("NO")
            return
    for i in r:
        if i not in l:
            print("NO")
            return
        if(l[i]!=r[i]):
            print("NO")
            return
    print("YES")
    print(ans)

    print(a)
solve()