
def kk(a,b):
    if(a=='' or b==''):
        return(0)
    res=0
    print('trying',a,b)
    diff = abs(int(b,2)-int(a,2))
    if(a[0]!=b[0]):
        if(a[0]=='0'):
            ia = (int(a,2))
            ib = int(b,2)
            orr = ia|ib
            res+=1
            ia = (orr)
            ba = bin(ia)[2:]
            print('orring')
            returned = kk(ba[1:],b[1:])
            res+=returned
        else:
            toadd = int('1'+'0'*(len(b)-1),2) - int(b,2)
            res+=toadd
            print('adding',toadd)
            ib = int('1'+'0'*(len(b)-1),2)
            returned = kk(a[1:],bin(ib)[3:])
            res+=returned
    else:
        print('equal')
        returned = kk(a[1:],b[1:])
        res+=returned
    return(min(res,diff))
def solve():
    a,b=map(int,input().split())
    la=bin(a)[2:]
    lb=bin(b)[2:]
    la = str.rjust(la,len(lb),'0')

    ress = kk(la,lb)
    print(ress)
for _ in range(int(input())):
    solve()