def solve():
    n = int(input())
    s = list(input())
    counts = {}
    if(n%2!=0):
        print("NO")
        return
    for i in range(n):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    for item in counts:
        if(counts[item]>n/2):
            print("NO")
            return
    s.sort()
    s1 = s[:n//2]
    s2 = s[n//2:]
    s2.reverse()
    r = s1+s2
    print("YES")
    print("".join(r))
for _ in range(int(input())):
    solve()