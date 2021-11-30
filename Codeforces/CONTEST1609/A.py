t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    pows=[]
    primes=[]
    total=sum(arr)
    for item in arr:
        i=0
        while(item%2==0):
            item//=2
            i+=1
        pows+=[i]
        primes+=[item]
    totalpows=sum(pows)
    primesum=sum(primes)
    highestt=0
    for i in range(len(arr)):
        total=primesum-primes[i]+arr[i]*pow(2,totalpows-pows[i])
        highestt=max(total,highestt)
    print(highestt)