t=int(input())
x=0
for _ in range(t):
    if(input().find('-')>-1):
        x-=1
    else:
        x+=1
print(x)