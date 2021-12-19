n = int(input())
a=list(map(int,input().split()))
highest=0
for l in range(len(a)+1):
    for r in range(l+1,len(a)+1):
        # print('leftpart',a[:l])
        # print('midpart',a[l:r])
        # print('rightpart',a[r:])
        # print('midsum',r-l-sum(a[l:r]))
        val = sum(a[:l])
        val += sum(a[r:])
        val += r-l - sum(a[l:r])
        highest = max(highest,val)
print(highest)