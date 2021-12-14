t=int(input())
for _ in range(t):
    l=int(input())
    a=input().split(" ")
    res=[a[0][0],a[0][1]]
    for i in range(1,len(a)):
        if(res[-1] == a[i][0]):
            res+=a[i][1]
        else:
            res+=a[i][0]
            res+=a[i][1]
    if(len(res)!=l):
        res+='a'
    print("".join(res))