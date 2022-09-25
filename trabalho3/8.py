# Vlw, Nicolas
x, y, z, r = input().split()
x, y, z, r = int(x), int(y), int(z), int(r)
s = 0

for X in range(x - r, x + r + 1):
    for Y in range(y - r, y + r + 1):
        for Z in range(z - r, z + r + 1):
            if (X - x) ** 2 + (Y - y) ** 2 + (Z - z) ** 2 <= r ** 2:
                s += 1
print(s)