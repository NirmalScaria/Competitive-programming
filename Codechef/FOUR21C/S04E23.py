t=int(input())
for _ in range(t):
    n,p,q=map(int,input().split())
    s=input()
    axis1count=0
    axis2count=0
    pres=1
    for item in s:
        if(item=='0'):
            pres*=-1
        if(pres==-1):
            axis1count+=1
        else:
            axis2count+=1
    # print(axis1count,axis2count)
    # 1 is p
    if(axis1count>=abs(p) and axis1count%2==p%2 and axis2count>=abs(q) and axis2count%2==q%2):
        print("YES")
    elif(axis2count>=abs(p) and axis2count%2==p%2 and axis1count>=abs(q) and axis1count%2==q%2):
        print("YES")
    else:
        print("NO")
    