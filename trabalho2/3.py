x1, y1 = input().split()
x2, y2 = input().split()
x3, y3 = input().split()

x1, y1, x2, y2, x3, y3 = float(x1), float(y1), float(x2), float(y2), float(x3), float(y3)

if ( x1 == x2 == x3) or (y1 == y2 == y3):
    print("não triângulo")
    exit(0)
else:
    print("triângulo")

l1 = ((x1-x2)**2 + (y1-y2)**2)**0.5
l2 = ((x1-x3)**2 + (y1-y3)**2)**0.5
l3 = ((x3-x2)**2 + (y3-y2)**2)**0.5

# vlw, Nicolas
if l1 == l2 == l3:
    print("equilátero")
elif l3 == l2 or l2 == l1 or l1 == l3:
    print("isósceles")
elif l1 != l2 != l3:
    print("escaleno")

