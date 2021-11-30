while(True):
    k=input()
    k=[int(i) for i in k]
    res=[]
    while(len(k)>1):
        if(k[0]<k[-1]):
            res=[k[0]]+res
            k=k[1:]
        else:
            res=res+[k[-1]]
            k=k[:-1]
    print(res+k)
    print(k+res)