import math

x1, y1, r1 = input().split()
x2, y2, r2 = input().split()


x1, y1, r1 = float(x1), float(y1), float(r1)
x2, y2, r2 = float(x2), float(y2), float(r2)

dist = math.hypot(x1-x2, y1-y2)

if dist <= r1+r2:
    print("S")
else:
    print("N")
