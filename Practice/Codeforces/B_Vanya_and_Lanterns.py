n,l = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
a=a
d=[]
for i in range(1,len(a)):
   d+=[a[i]-a[i-1]]
if(d==[]):
    res = 0
else:
    res = max(d)/2
res = max(res, a[0], l-a[-1])
print(res)