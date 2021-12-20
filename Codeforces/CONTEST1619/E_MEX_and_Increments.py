def solve():
    n=int(input())
    a = list(map(int,input().split()))
    d = {}
    for item in a:
        if(item in d):
            d[item]+=1
        else:
            d[item]=1
    for i in range(n+1):
        if(i not in d):
            d[i]=0
    extras = []
    tobeadded = 0
    for i in range(n+1):
        if(d[i]==0):
            print(0+tobeadded,end=" ")
            if(extras == []):
                break
            k=extras.pop()
            tobeadded+=i-k
        else:
            
            print(d[i]+tobeadded, end=" ")
            if(d[i]>1):
                extras+=[i]*(d[i]-1)
    print("-1 "*(n-i), end="")
    print()
for _ in range(int(input())):
    solve()