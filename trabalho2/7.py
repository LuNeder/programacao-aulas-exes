l1, c1 = input().split()
l2, c2 = input().split()

l1, c1, l2, c2 = int(l1), int(c1), int(l2), int(c2)

if abs(l1 - l2) < 2 and abs(c1 - c2) < 2:
    print("SIM")
else:
    print("NÃO")