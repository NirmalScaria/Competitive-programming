def solve():
    k = [int(i) for i in list(input())]
    for i in range(len(k)-2, -1, -1):
        if(k[i]+k[i+1]>9):
            res = k[:i] + [k[i]+k[i+1]] + k[i+2:]
            print("".join([str(x) for x in res]))
            return
    res = [k[0] + k[1]] + k[2:]
    print("".join([str(x) for x in res]))
    return
for _ in range(int(input())):
    solve()