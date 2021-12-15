t=int(input())
for _ in range(t):
    n=int(input())
    arr = list(map(int,input().split()))
    occurences={}
    for i in range(len(arr)):
        if(arr[i] in occurences):
            occurences[arr[i]]+=[i]
        else:
            occurences[arr[i]]=[-1,i]
    subsequenceCount=0
    for uniqueValue in occurences:
        occurences[uniqueValue]+=[n]
        leftPointer=1
        rightPointer=uniqueValue
        while(rightPointer<len(occurences[uniqueValue])-1):
            subSequenceCount = (occurences[uniqueValue][leftPointer] - occurences[uniqueValue][leftPointer-1]) * (occurences[uniqueValue][rightPointer+1] - occurences[uniqueValue][rightPointer]) * uniqueValue
            subsequenceCount+=subSequenceCount
            rightPointer+=1
            leftPointer+=1
    print(subsequenceCount)