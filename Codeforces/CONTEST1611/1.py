t=int(input())
for _ in range(t):
    k=input()
    if( (int(k[-1])) % 2 == 0 ):
        print(0)
    elif(int(k[0])%2==0):
        print(1)
    else:
        i=0
        for item in k:
            if(int(item)%2==0):

                print(2)
                break
            i+=1
        if(i==len(k)):
            print(-1)