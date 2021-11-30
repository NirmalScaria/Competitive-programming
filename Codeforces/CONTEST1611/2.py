t = int(input())
for _ in range(t):
    a,b=map(int,input().split())
    res=0
    print(min(a,b,(a+b)//4))