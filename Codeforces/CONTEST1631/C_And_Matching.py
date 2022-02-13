def solve():
    n , k = map(int,input().split())
    if(n==4 and k==3):
        print(-1)
        return
    if(k==n-1):
        print(n-1,n-2)
        print(1,n-3)
        print(2,0)
        n//=2
        a=n
        b=a-1
        i=3
        while(i<n):
            print(a,b)
            i+=1
            a+=1
            b-=1
        return
    if(k==0):
        for i in range(n//2):
            print(i,(n-1)^i)
    else:
        a=1
        b=n-2
        print(k,n-1)
        n//=2
        i=1
        while(i<n):
            if(a==k):
                print(0,b)
            else:
                if(b==k):
                    print(0,a)
                else:
                    print(a,b)
            i+=1
            a+=1
            b-=1
for _ in range(int(input())):
    solve()