from math import sqrt
a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

deltha = (b ** 2) - (4 * a * c)

if deltha < 0:
    print("No real roots.")
    exit(0)

x1 = ((0 - b) - sqrt(deltha)) / (2 * a)
x2 = ((0 - b) + sqrt(deltha)) / (2 * a)

if x1 == x2:
    print("%.2f" % x2)
else:
    print("%.2f" % x1)
    print("%.2f" % x2)
