import statistics
def solve():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    freq = {}
    for num in a:
        if(num in freq):
            freq[num]+=1
        else:
            freq[num]=1
    print(freq)
    x = min(a)
    y = max(a)
    included_count = n
    while(included_count > n/2):
        if(x not in freq):
            x+=1
            continue
        if(y not in freq):
            y-=1
            continue
        if(freq[x]<freq[y]):
            if(included_count - freq[x] > n/2):
                included_count -= freq[x]
                x+=1
            else:
                break
        else:
            if(included_count -freq[y] > n/2):
                included_count -= freq[y]
                y-=1
            else:
                break
    print(x,y)
    
for _ in range(int(input())):
    solve()