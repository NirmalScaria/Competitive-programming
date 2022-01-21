def solve():
    n = int(input())
    k = list(map(int,input().split()))
    h = list(map(int,input().split()))
    nn = []
    for i in range(len(k)):
        nn += [[k[i]-h[i], k[i]]]
    b = []
    nn.sort(key = lambda x:x[0])
    m = []
    s = -10000
    max = -100000
    for i in range(len(nn)):
        a = nn[i]
        if a[0] >= max:
            if i != 0:
                m.append([s,max])
            max = a[1]
            s = a[0]
        else:
            if a[1] >= max:
                max = a[1]
    if max != -100000 and [s, max] not in m:
        m.append([s, max])
    res = 0
    # print(m)
    for item in m:
        dist = abs(item[1] - item[0])
        res += (dist * (dist+1))//2
    print(res)
for _ in range(int(input())):
    solve()