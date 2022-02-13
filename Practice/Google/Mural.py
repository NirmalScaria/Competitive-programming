def solve():
    n = int(input())
    a = list(map(int,input()))
    window_length = (n+1)//2
    window_sum = sum(a[:window_length])
    max_sum = window_sum
    for i in range(window_length,n):
        window_sum += a[i]
        window_sum -= a[i-window_length]
        max_sum = max(max_sum,window_sum)
    return(max_sum)
for i in range(int(input())):
    ans = solve()
    print("Case #"+str(i+1)+": "+str(ans),sep="")