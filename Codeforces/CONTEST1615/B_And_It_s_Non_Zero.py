def solve():
    l,r= map(int,input().split())
    po = 1
    mzcnt = 100000000000
    while(po<=r):
        po*=2
        rzcnt = (r-(r%po))//2 + min((r%po)+1,po//2)
        # print(r,'count is ',rzcnt, 'wioth',po)
        lzcnt = (l-1-((l-1)%po))//2 + min(((l-1)%po)+1,po//2)
        mzcnt = min(mzcnt,rzcnt-lzcnt)
        
    print(mzcnt)
for _ in range(int(input())):
    solve()