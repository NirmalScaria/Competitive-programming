def solve():
    m , xa = map(int,input().split())
    lastres = 1
    m-=1
    for i in range(2,xa+1):
        print(lastres,end=" ")
        removedfirst = m%i +1
        if(lastres >=removedfirst):
            lastres+=1
    print(lastres,end=" ")
for _ in range(int(input())):
    solve()