t=int(input())
for _ in range(t):
    n,k,x = map(int,input().split())
    s = list(input())
    arr = []
    i=0
    if(x==1):
        s="".join(s)
        s=s.replace("*","")
        print(s)
        continue
    x-=1
    while(i<len(s)):
        if(s[i]!='*'):
            arr+=[s[i]]
            i+=1
        else:
            count=1
            while(i<len(s) and s[i]=='*'):
                i+=1
                count+=1
            arr+=[(count-1)*k]
    i = len(arr)-1 
    remaining = x
    while(i>=0):
        if(arr[i]=='a'):
            i-=1
            continue
        nn = arr[i]
        kk = remaining % (nn+1)
        arr[i] = 'b'*int(kk)
        remaining=remaining//(nn+1)
        if(remaining==0):
            break
        i-=1
    print("".join(arr))