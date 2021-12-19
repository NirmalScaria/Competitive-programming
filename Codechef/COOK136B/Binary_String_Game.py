t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    maxPossibleBitflips = n-1
    bitflips=0
    for i in range(1,len(s)):
        if(s[i]!=s[i-1]):
            bitflips+=1

    # print("present bitflips",bitflips)
    # print("max bitflips",maxPossibleBitflips)
    winn=0
    moves = (maxPossibleBitflips-bitflips+1)//2
    if(moves%2==0):
        winn = 1
    else:
        winn =0
    # if((maxPossibleBitflips-bitflips)%2==1):
    #     winn=1-winn
    if(winn==0):
        print("JJ")
    else:
        print("Uttu")