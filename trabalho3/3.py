n = int(input())
div = []
num = 0

for i in range(2, n):
    if n % i == 0:
        div.append(i)

for i in div:
    num += 1
    
if num == 0:
    print("primo")
else:
    for i in div:
        print(i)
    
