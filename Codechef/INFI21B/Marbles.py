def solve():
    n=int(input())
    s=list(input())
    p=list(input())
    vowels = {'a','e','o','i','u'}
    d = {}
    vowscore = 0
    conscore = 0
    alp='abcdefghijklmnopqrstuvwxyz'
    for item in alp:
        d[item]=0
    for i in range(n):
        if(s[i]=='?' and p[i]=='?'):
            vowscore+=2
            conscore+=2
        elif(s[i]=='?' and p[i]!='?'):
            d[p[i]]+=2
            if(p[i] in vowels):
                conscore+=1
            else:
                vowscore+=1
        elif(s[i]!='?' and p[i]=='?'):
            d[s[i]]+=2
            if(s[i] in vowels):
                conscore+=1
            else:
                vowscore+=1
    for letr in d:
        if(letr in vowels):
            d[letr]+=vowscore
        else:
            d[letr]+=conscore
    bestletter = 'a'
    bestletterscore = 0
    for item in d:
        if(d[item]>bestletterscore):
            bestletterscore=d[item]
            bestletter=item
    # print('best leter is ', bestletter)
    for i in range(n):
        if(s[i]=='?'):
            s[i]=bestletter
        if(p[i]=='?'):
            p[i]=bestletter
    res=0
    for i in range(n):
        if(s[i]!=p[i]):
            issvowel=0
            ispvowel=0
            if s[i] in vowels:
                issvowel=1
            if(p[i] in vowels):
                ispvowel=1
            if(issvowel==1):
                if(ispvowel==1):
                    res+=2
                else:
                    res+=1
            else:
                if(ispvowel==1):
                    res+=1
                else:
                    res+=2
    print(res)
for _ in range(int(input())):
    solve()