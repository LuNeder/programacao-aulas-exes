lst = []
f = 0
sp = 0
si = 0
vet = ""

while True:
    a = int(input())
    if a < 0:
        break
    else:
        lst.append(a)



# Maior que 5
for i in lst:
    if i > 5:
        f += 1
    
print(f)


# Soma dos pares
for i in lst:
    if i % 2 == 0:
        sp += i
print(sp)

# Soma dos impares
for i in lst:
    if i % 2 != 0:
        si += i
print(si)

# Len
print(len(lst))

# Vet
for i in lst:
    vet = vet + str(i) + " "
print(vet)