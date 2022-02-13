def solve():
    s = list(input())
    zcount = s.count('0')
    if(zcount!=len(s)/2):
        print(min(zcount,len(s)-zcount))
        return
    zca = zcount - (s[0]=='0')
    print(min(zca,len(s)-zca-1))
for _ in range(int(input())):
    solve()