def solve():
    n = int(input())
    a = []
    for _ in range(n):
        a.append((input()))
    s  = {}
    # count a to s
    for item in a:
        if(item in s):
            s[item] += 1
        else:
            s[item] = 1
    for item in a:
        if(len(item)==1):
            print("YES")
            return
        if(len(item)==2):
            if(item[0]==item[1]):
                print("YES")
                return
            if(item[::-1] in s and s[item[::-1]]>0):
                print("YES")
                return
            for x in range(ord('a'),ord('z')+1):
                t = chr(x)
                if(t+item[::-1] in s and s[t+item[::-1]]>0):
                    print("YES")
                    return
        if(len(item)==3):
            if(item[0]==item[2]):
                print("YES")
                return
            if(item[::-1] in s and s[item[::-1]]>0):
                print("YES")
                return
            if(item[1]+item[0] in s and s[item[1]+item[0]]>0):
                print("YES")
                return
        s[item]-=1
    print("NO")
for _ in range(int(input())):
    solve()