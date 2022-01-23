def solve():
    l , r , k = map(int,input().split())
    if(l-r==0):
        if(l==1):
            print("NO")
            return
        else:
            print("YES")
            return
    needed = 0
    if(l%2==1 or r%2==1):
        needed+=1
    needed+= (r-l)//2
    # print("needed",needed)
    if(k>=needed):
        print("YES")
    else:
        print("NO")
for _ in range(int(input())):
    solve()