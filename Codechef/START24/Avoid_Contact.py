def solve():
    x,y = map(int,input().split())
    if(y==0):
        print(x)
    elif(y==1):
        print(x+1)
    elif(y==2):
        print(x+2)
    else:
        print(x + (y*2) -2)
for _ in range(int(input())):
    solve()