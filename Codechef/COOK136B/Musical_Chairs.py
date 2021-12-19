import math
t=int(input())
for _ in range(t):
    n=int(input())
    n-=1
    count=0
    i=1
    for i in range(1,int(math.sqrt(n))+1):
        if(n%i==0):
            if(n/i==i):
                count+=1
            else:
                count+=2
    print(count)