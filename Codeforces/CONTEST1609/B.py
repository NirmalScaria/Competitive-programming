n,q=map(int,input().split())
s=input()
starts=set()
for i in range(len(s)-2):
    if(s[i:i+3]=="abc"):
        starts.add(i)
s=list(s)
tochange=len(starts)
for _ in range(q):
    i,l=input().split()
    i=int(i)
    i-=1
    if(l!=s[i]):
        if(s[i]=='a' and starts.discard(i)==i):
            tochange-=1
        elif(s[i]=='b' and starts.discard(i-1)==i-1):
            tochange-=1
        elif(s[i]=='c' and starts.discard(i-2)==i-2):
            tochange-=1
        if(l=='a' and i<len(s)-2 and s[i+1]=='b' and s[i+2]=='c'):
            starts.add(i)
            tochange+=1
        if(l=='b' and i<len(s)-1 and i>0 and s[i+1]=='c' and s[i-1]=='a'):
            starts.add(i-1)
            tochange+=1
        if(l=='c' and i>1 and s[i-1]=='b' and s[i-2]=='a'):
            starts.add(i-2)
            tochange+=1
        s[i]=l
    print(len(starts))