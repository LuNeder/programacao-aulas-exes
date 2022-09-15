import math

r, t = input().split()
r, t = float(r), float(t)

a = r * math.cos(t)
b = r * math.sin(t)

sinal = "+"

if b < 0:
    sinal ="-"
    b = abs(b)
    
print("%.2f %s %.2fi" % (a, sinal, b))
