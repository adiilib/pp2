import math

r = float(input())
x1,y1 = map(float,input().split())
x2,y2 = map(float,input().split())

dx,dy = x2-x1, y2-y1
a,b = dx, dy
A = a**2 + b**2
B = 2*(a*x1 + b*y1)
C = x1**2 + y1**2 - r**2

D = B**2 - 4*A*C
if D <= 0:
    print("0.0000000000")
else:
    sqrtD = math.sqrt(D)
    t1 = (-B - sqrtD)/(2*A)
    t2 = (-B + sqrtD)/(2*A)
    t1, t2 = max(0,min(t1,t2)), min(1,max(t1,t2))
    if t2 < t1:
        print("0.0000000000")
    else:
        lx = dx*(t2-t1)
        ly = dy*(t2-t1)
        print(f"{math.hypot(lx,ly):.10f}")