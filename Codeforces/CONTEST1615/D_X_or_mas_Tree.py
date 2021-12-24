class Node:
    def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
    def PrintTree(self):
      print(self.data)
def solve():
    n,m=map(int,input().split())
    edges = []
    elves = []
    for _ in range(n-1):
        edges+= [list(map(int,input().split()))]
        # edges[str(min(t[0],t[1]))+'.'+str(max(t[0],t[1]))]=t[2]
    for _ in range(m):
        elves+=[list(map(int,input().split()))]
    elves.sort(key = lambda x: abs(x[1]-x[0]))
    # print(edges)
    edges.sort(key=lambda x: min(x[0],x[1]))
    arr = {1:Node(1)}
    for item in edges:
        l = min(item[0],item[1])
        r = max(item[0],item[1])
        arr[r]=Node(r)
        if(arr[l].left==None):
            arr[l].left=arr[r]
        else:
            arr[l].right=arr[r]
    
for _ in range(int(input())):
    solve()