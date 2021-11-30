def rec(rem,res):
    if(res==[]):
        # print('initial start')
        # print(rem,res)
        tmp=rec(rem[1:], [rem[0]])
        if(tmp != -1):
            return(tmp)
        tmp= rec(rem[:-1], [rem[-1]])
        
        return(tmp)
    if(rem==[]):
        return(res)
    # Trying left
    if( rem[0] < res[-1] ):
        # print("going left from ",rem,res)
        tmp = rec(rem[1:] , [rem[0]]+res)
        if(tmp!=-1):
            return(tmp)
    # trying right
    if( rem[-1] < res [0]):
        # print("going right from", rem , res)
        tmp = rec(rem[:-1] , res + [rem[-1]])
        if(tmp!=-1):
            return(tmp)
    return(-1)
        

t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=[]
    ress=rec(a,res)
    if(ress==-1):
        print(ress)
    else:
        ress=[str(i) for i in ress]
        print(" ".join(ress))