def solve():
    a,s = map(list,input().split())
    a=['0']*20+a
    # print(a)
    i=len(a)-1
    j=len(s)-1
    res=[]
    while(j>=0):
        if(a[i]==s[j]):
            res=[0]+res
            i-=1
            j-=1
        elif(a[i]<s[j]):
            res=[int(s[j])-int(a[i])] + res
            i-=1
            j-=1
        else:
            if(j==0 or s[j-1]!='1'):
                print(-1)
                return
            k = 10 + int(s[j])
            res = [k-int(a[i])] + res
            j-=2
            i-=1
    if(a[:i+1].count('0') != len(a[:i+1])):
        print(-1)
        return
    print(int("".join([str(x) for x in res])))
    

for _ in range(int(input())):
    solve()