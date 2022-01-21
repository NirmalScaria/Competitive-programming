def solve():
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for i in range(n-1):
        xxx, yyy = map(int,input().split())
        graph[xxx] += [(xxx,yyy,i)]
        graph[yyy] += [(yyy,xxx,i)]
    for item in graph:
        if(len(item)>2):
            print(-1)
            return
    cur = 1
    while(len(graph[cur])!=1):
        cur+=1 
    prev = cur
    ans = [0 for _ in range(n-1)]
    for k in range(n-1):
        for  x,y,i in graph[cur]:
            if(y!=prev):
                ans[i]=str([2,3][k%2])
                prev = cur
                cur = y
                break
    print(" ".join(ans)) 
for _ in range(int(input())):
    solve()