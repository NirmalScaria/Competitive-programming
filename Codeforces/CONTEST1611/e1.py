t=int(input())
for _ in range(t):
    input()
    n,k = map(int,input().split())
    friends=list(map(int,input().split()))
    connects = [[] for _ in range(n+1)]
    for _ in range(n):
        f,t=map(int,input().split())
        connects[f]+=[t]
        connects[t]+=[f]
    print(connects)