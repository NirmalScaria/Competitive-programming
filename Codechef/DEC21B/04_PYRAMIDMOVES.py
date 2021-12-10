import math
def findIndex(t):
    x=(t-1)*2
    if(1+4*(x)<0):
        ind1=0
    else:
        k=math.sqrt(1+4*x)
        if(-1+k>=0):
            ind1=(-1+k)//2

        else:
            ind1=(-1+k)//2
    first=(ind1*(ind1+1))//2 + 1
    ind2=t-first
    return((int(ind1),int(ind2)))
t=int(input())
for _ in range(t):
    s,e=map(int,input().split())
    if(s>e):
        print(0)
        continue
    if(s==e):
        print(1)
        continue
    sr,sc=findIndex(s)
    er,ec=findIndex(e)
    if(sc + (er-sr) < ec or ec<sc):
        print(0)
        continue
    i=er-sr
    j=ec-sc
    # print('n=',i,'r=',j)
    numerator=denominator=1
    for x in range(j):
        numerator=(numerator * (i-x)) % 1000000007
        denominator=(denominator * (x+1)) % 1000000007
    res=( numerator * pow(denominator,1000000007-2,1000000007) ) % 1000000007
    print(res)