num = input()
d = []

for i in num:
    d.append(i)

n = len(d)

nam = 0
for i in d:
    nam = nam + int(i)**n

if str(nam) == num:
    print("True")
else:
    print("False")