n = int(input())
a = list(map(int,input().split()))
res = [[0 for _ in range(n)] for _ in range(n)]
print(a)
for i in range(n):
    for j in range(i):
        if(a[i]==a[j]):
            res[i][j]=1
for item in res:
    print(item)