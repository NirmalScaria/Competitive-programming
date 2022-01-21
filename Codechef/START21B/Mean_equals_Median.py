import math
def solve():
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    total = sum(a)
    toAddToReachMultiple = total%n
    mean = total / n
    mednposn = (n-1)//2
    median = a[mednposn]

    if(mean<median):
        print(n*median -total)
    else:
        cent = median
        mn = mean
        remsum = total - median
        while(mn>cent):
            cent = math.ceil(mn)
            mn = (remsum+cent)/n
            print('median',cent)
            print('mean',mn)
        print(cent*n-total)
for _ in range(int(input())):
    solve()