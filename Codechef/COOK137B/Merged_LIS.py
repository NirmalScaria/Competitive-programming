import bisect
def LIS(nums):
    dp=[]
    for i,num in enumerate(nums):
        idx=bisect.bisect_right(dp,num)
        if idx==len(dp): dp.append(num)
        else: dp[idx]=num
    return len(dp)

def solve():
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print(LIS(a)+LIS(b))
for _ in range(int(input())):
    solve()