t=int(input())
for _ in range(t):
    n=int(input())
    a = list(map(int,input().split()))
    isdiff=0
    for item in a:
        if(item != a[0]):
            isdiff=1
    if(isdiff==0):
        print(0)
    elif(max(a) == a[-1]):
        print(1)
    else:
        print(2)