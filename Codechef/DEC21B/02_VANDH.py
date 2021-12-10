t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    if(n==m):
        print(2*(n+1))
        print('01'*(n+1))
    elif(n>m):
        res=''
        res+='01'*m
        res+='010'*(n-m)
        print(len(res))
        print(res)
    else:
        res=''
        res+='10'*n
        res+='101'*(m-n)
        print(len(res))
        print(res)