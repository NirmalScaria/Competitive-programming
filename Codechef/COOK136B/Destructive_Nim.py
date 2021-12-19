t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    count =0 
    for item in a:
        if(item==1):
            count+=1
    if(count==0):
        # print("yo")
        print("Utkarsh")
        continue
    if(count==n):
        if(count%2==1):
            print("Utkarsh")
        else:
            print("Ashish")
        continue
    if(count%2==1):
        print("Ashish")
    else:
        print("Utkarsh")