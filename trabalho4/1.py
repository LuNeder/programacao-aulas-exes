lst = [int(i) for i in input().split()]


maxi = max(lst)
vnnum = lst.count(lst[len(lst) - 1])
soma = sum(lst)
ind = ""
indices = []

for i, bird in enumerate(lst):
    if bird == maxi:
        indices.append(i)


print(soma)
print(vnnum)
print(maxi)

for i in indices:
    ind = ind + str(i) + " " 

print(ind)
