t=int(input())
for _ in range(t):
    n,l,r,k=map(int,input().split())
    values = [int(i) for i in input().split() if int(i)>=l and int(i)<=r]
    values.sort()
    i=0
    for item in values:
        if(item<=k):
            k-=item
            i+=1
        else:
            break
    print(i)