n,k=map(int,input().split())
res=0
a = list(map(int,input().split()))
for item in a:
    if(item>0 and item>=a[k-1]):
        res+=1
print(res)