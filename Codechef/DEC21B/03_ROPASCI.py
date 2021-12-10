t=int(input())
for _ in range(t):
    n=int(input())
    s=list(input())
    dp=[i for i in range(n)]
    if(s[-1]=='R'):
        dp[-1]=['R','P','R']
    elif(s[-1]=='P'):
        dp[-1]=['P','P','S']
    else:
        dp[-1]=['R','S','S']
    for i in range(n-2,0,-1):
        if(s[i]=='R'):
            dp[i]=[dp[i+1][0]]+[dp[i+1][1]]+[dp[i+1][0]]
        elif(s[i]=='P'):
            dp[i]=[dp[i+1][1]]+[dp[i+1][1]]+[dp[i+1][2]]
        else:
            dp[i]=[dp[i+1][0]]+[dp[i+1][2]]+[dp[i+1][2]]
    res=''
    for i in range(n-1):
        if(s[i]=='R'):
            res+=dp[i+1][0]
        elif(s[i]=='P'):
            res+=dp[i+1][1]
        else:
            res+=dp[i+1][2]
    res+=s[-1]
    print(res)