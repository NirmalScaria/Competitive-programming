t=int(input())
for _ in range(t):
    n=int(input())
    k=[]
    for _ in range(n):
        k+=[input()]
    toUp=[[0 for _ in range(n)] for _ in range(n)]
    toLeft=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        if(k[i][0]=='1'):
            toLeft[i][0]=1
        if(k[0][i]=='1'):
            toUp[0][i]=1
        for j in range(1,n):
            if(k[i][j]=='1'):
                toLeft[i][j]=toLeft[i][j-1]+1
            if(k[j][i]=='1'):
                toUp[j][i]=toUp[j-1][i]+1
    count=0
    for i in range(n):
        for j in range(n):
            if(k[i][j]=='1'):
                count+=1
                ttt=min(min(i,j)+1,toUp[i][j],toLeft[i][j])
                for kk in range(1,ttt):
                    if(toLeft[i-kk][j] > kk and toUp[i][j-kk]>kk):
                        count+=1
    print(count)