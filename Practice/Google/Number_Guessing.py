t = int(input())
for i in range(t):
    l,r = map(int,input().split())
    r+=1
    n = int(input())
    while(l<=r):
        mid = (l+r)//2
        print(mid)
        resp = input()
        if(resp == 'TOO_SMALL'):
            l = mid+1
        elif(resp == 'TOO_BIG'):
            r = mid-1
        else:
            break