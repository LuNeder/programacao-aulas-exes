n = int(input())
div = []
num = 0

for i in range(1, n):
    if n % i == 0:
        div.append(i)

for i in div:
    num += 1

sum = 0
for i in div:
    sum = sum + i
if sum == n:
    print("True")
else:
    print("False")