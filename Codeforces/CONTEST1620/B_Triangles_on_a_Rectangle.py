t=int(input())
for _ in range(t):
    w,h=map(int,input().split())
    xs = list(map(int,input().split()))[1:]
    xe = list(map(int,input().split()))[1:]
    ys = list(map(int,input().split()))[1:]
    ye = list(map(int,input().split()))[1:]
    xmax = max((xs[-1]-xs[0]), (xe[-1]-xe[0]))
    ymax = max((ys[-1]-ys[0]), (ye[-1]-ye[0]))

    res = max(ymax*w, xmax*h)
    print(res)