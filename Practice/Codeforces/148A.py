k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())

ls=[k,l,m,n]
res=0
for item in ls:
    res+=d//item
print('r1',res)
for i in ls:
    for j in ls:
        if(i%j!=0 and j%i!=0):
            res-=d//(i*j)
print('r2',res)
for i in ls:
    res+=d//(k*l*m*n//i)

res-=d//(k*l*m*n)
print(res)