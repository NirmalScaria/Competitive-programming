def solve():
    n = int(input())
    if(n%7==0):
        print(n)
        return
    s = str(n)
    if(n<100):
        for i in range(10):
            if(int(s[0]+str(i))%7==0):
                print(int(s[0]+str(i)))
                return
        for i in range(10):
            if(int(str(i)+s[1])%7==0):
                print(int(str(i)+s[1]))
                return
    else:
        for i in range(10):
            if(int(s[0]+s[1]+str(i))%7==0):
                print(int(s[0]+s[1]+str(i)))
                return
        for i in range(10):
            if(int(s[0]+str(i)+s[2])%7==0):
                print(int(s[0]+str(i)+s[2]))
                return
        for i in range(10):
            if(int(str(i)+s[1]+s[2])%7==0):
                print(int(str(i)+s[1]+s[2]))
                return
    for i in range(10):
        for j in range(10):
            if(int(str(i)+str(j)+s[2])%7==0):
                print(int(str(i)+str(j)+s[2]))
                return

        for j in range(10):
            if(int(str(i)+s[1]+str(j))%7==0):
                print(int(str(i)+s[1]+str(j)))
                return
        for j in range(10):
            if(int(s[0]+str(i)+str(j))%7==0):
                print(int(s[0]+str(i)+str(j)))
                return
    print('777')


for _ in range(int(input())):
    solve()