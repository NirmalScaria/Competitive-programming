t=int(input())
for _ in range(t):
    n=int(input())
    a = list(map(int,input().split()))
    abc = sum(a) // (((n+1)*n)//2)
    res=[]
    flag = 0
    for i in range(n-1):
        ans = a[i] + abc - a[i+1]
        if(ans%n !=0 or ans ==0):
            flag = 1
            print("NO")
            break
        ans //= n
        res=res+[ans]
    if(flag ==0 ):
        ans = a[-1] + abc - a[0]
        if(ans % n != 0 or ans==0):
            flag = 1
            print("NO")
        ans//=n
        res=[ans]+res
        res = [str(i) for i in res]
        print("YES")
        print(" ".join(res))