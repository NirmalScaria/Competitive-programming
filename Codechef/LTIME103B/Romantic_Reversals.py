def solve():
    n,k = map(int,input().split())
    s = input()
    m=k//2
    d=k
    a = m-1
    if(k%2==1):
        print(s[m],end="")
        m+=1
        k-=1
    for i in range(k):
        if(i%2==1):
            print(s[a],end="")
            a-=1
        else:
            print(s[m],end="")
            m+=1
    print(s[d:n])
for _ in range(int(input())):
    solve()