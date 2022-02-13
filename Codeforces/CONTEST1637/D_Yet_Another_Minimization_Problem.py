def calculateSum(a,b):
    suma = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            suma+=(a[i]+a[j])**2
    sumb=0
    for i in range(len(b)):
        for j in range(i+1,len(b)):
            sumb += (b[i]+b[j])**2
    return(suma+sumb)
def solve():
    n = int(input())
    a = list(map(int,input().split()))
    b= list(map(int,input().split()))
    bestres = calculateSum(a,b)
    for i in range(n):
        if(a[i]<b[i]):
            temp = a[i]
            a[i] = b[i]
            b[i] = temp
    print(a)
    print(b)
    differences = [a[i]-b[i] for i in range(n)]
    
for _ in range(int(input())):
    solve()