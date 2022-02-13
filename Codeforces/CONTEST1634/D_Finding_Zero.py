def solve():
    input()
    n=int(input())
    # Assuming [1] is 0
    maxval = 0
    maxpos = 2
    for i in range(2,n+1):
        # Checing if [i] is zero
        print('to check if',i,'is zero')
        first = (i+1)
        second = (i+2)
        if(first>n):
            first = first%(n+1)
            first+=2
        if(second>n):
            second = second%(n+1)
            second+=2
        print('first',first,'second',second)
        print(i,first,second)
        including = int(input())
        print(1,first,second)
        excluding = int(input())
        if(including-excluding > maxval):
            maxval = including-excluding
            maxpos = i
    print(i)
for _ in range(int(input())):
    solve()