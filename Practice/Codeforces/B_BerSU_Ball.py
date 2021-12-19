n = int(input())
b=list(map(int,input().split()))
m = int(input())
g = list(map(int,input().split()))
b.sort()
g.sort()

count = 0
for item in b:
    less,eq,more = -1,-1,-1
    for i in range(len(g)):
        if(less == -1 and g[i] == item-1):
            less = i
            g = g[:i]+g[i+1:]
            count+=1
            break
        elif(eq==-1 and g[i]==item):
            eq = i
            g=g[:i]+g[i+1:]
            count+=1
            break
        elif(more==-1 and g[i]==item+1):
            more = i
            g=g[:i]+g[i+1:]
            count+=1
            break
            
print(count)