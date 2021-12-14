t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    flag=0
    for i in range(len(l)):
        if(flag!=0):
            break
        for j in range(i+1,len(l)):
            if(flag!=0):
                break
            for k in range(j+1,len(l)):
                t=l[:]
                t.remove(l[i])
                t.remove(l[j])
                t.remove(l[k])
                if(l[i]+l[j] in t):
                    
                    t.remove(l[i]+l[j])
                    if(l[i]+l[k] in t):
                        t.remove(l[i]+l[k])
                        if(l[j]+l[k] in t):
                            t.remove(l[j]+l[k])
                            if(l[i]+l[j]+l[k] in t):
                                print(l[i],l[j],l[k])
                                flag=1
                                break
                    