def solve():
    s=input()
    if(len(s)%2==1):
        print("NO")
        return
    if(s[:len(s)//2] == s[len(s)//2:]):
        print("YES")
        return
    print("NO")
for _ in range(int(input())):
    solve()