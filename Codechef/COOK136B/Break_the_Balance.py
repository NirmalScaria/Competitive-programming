t=int(input())
for _ in range(t):
    s = input()
    for i in range(len(s)-1,-1,-1):
        if(s[i]=='('):
            break
    print(len(s)-i-1)