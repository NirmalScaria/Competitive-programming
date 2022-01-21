def solve():
    n = int(input())
    a = [0]+list(input())
    b = [0]+list(input())
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    k = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0]=k[0][0]=0
    for i in range(1,n+1):
        if(a[i]=='1'):
            dp[0][i] = dp[0][i-1]
            k[0][i] = k[0][i-1]+1
        else:
            dp[0][i] = dp[0][i-1] + k[0][i-1]
            k[0][i] = k[0][i-1]
        if(b[i] =='1'):
            dp[i][0] = dp[i-1][0]
            k[i][0] = k[i-1][0] +1
        else:
            dp[i][0] = dp[i-1][0] + k[i-1][0]
            k[i][0] = k[i-1][0]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(b[i]=='1'):
                adp = dp[i-1][j]
                ak = k[i-1][j]+1
            else:
                adp = dp[i-1][j] + k[i-1][j]
                ak = k[i-1][j]
            if(a[j]=='1'):
                bdp = dp[i][j-1]
                bk = k[i][j-1] + 1
            else:
                bdp = dp[i][j-1] + k[i][j-1]
                bk = k[i][j-1]
            if(adp<bdp):
                dp[i][j] = adp
                k[i][j] = ak
            else:
                dp[i][j] = bdp
                k[i][j] = bk
    print(dp[-1][-1])
for _ in range(int(input())):
    solve()