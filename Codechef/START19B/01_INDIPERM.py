t=int(input())
for _ in range(t):
    n=int(input())
    if(n==2):
        k=[2,1]
    else:
        k=[i for i in range(2,n+1)]
        k=[1]+k[1:]+[k[0]]
    print(" ".join([str(i) for i in k]))