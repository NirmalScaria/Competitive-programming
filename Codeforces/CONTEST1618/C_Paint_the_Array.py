import math
def gcd (a,b):
    if (b == 0):
        return a
    else:
         return gcd (b, a % b)
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[a[i] for i in range(len(a)) if i%2==0]
    a=[a[i] for i in range(len(a)) if i%2!=0]
    lcm2=lcm1=1
    for item in a:
        lcm1*=item
    gdc1=gcd2=1
    gcd2 = b[0]
    for item in b[1::]:
        gcd2=gcd(gcd2, item)
    if(lcm1 % gcd2 !=0 ):
        # print("FOund")
        # print('gcd 2 is ',gcd2, 'lcm1', lcm1)
        print(gcd2)
        continue
    for item in b:
        lcm2*=item
    gcd1 = a[0]
    for item in a[1::]:
        gcd1 = gcd(gcd1,item)
    if(lcm2 % gcd1 !=0):
        print(gcd1)
        # print("gcd1 is ",gcd1,'lcm2 ',lcm2)
        continue
    print(0)