import math
t=int(input())
for _ in range(t):
    n = int(input())
    if(n==1):
        print(1)
    elif(n==2):
        print(2)
    elif(n==3):
        print(4)
    else:
        logval =math.floor(math.log2(n))
        # print('log is ',logval)
        # print('logval ', logval**2)
        if(2**logval== n):
            print((2**(logval+1) -1) %1000000007)
        else:
            print((2**(logval+1)) % 1000000007)