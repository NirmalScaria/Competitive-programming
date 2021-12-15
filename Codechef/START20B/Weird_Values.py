t=int(input())
for _ in range(t):
    n=int(input())
    a = list(map(int,input().split()))
    freq=[]
    d={}
    for i in range(len(a)):
        if(a[i] in d):
            d[a[i]]+=[i]
        else:
            d[a[i]]=[-1,i]
    result=0
    for item in d:
        if(len(d[item])<item):
            continue
        d[item]+=[n]
        l=1
        r=item
        # print('checking ',d[item],' for val',item)
        while(r<len(d[item])-1):
            # print('l , r are ',l,r)
            ans = (d[item][l] - d[item][l-1]) * (d[item][r+1] - d[item][r]) * item
            result+=ans
            # print('added ',ans)
            r+=1
            l+=1
            
    print(result)