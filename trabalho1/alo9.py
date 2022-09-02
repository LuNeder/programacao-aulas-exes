ordinais = ["primeiro", "segundo", "terceiro", "quarto"]
num  = input()

indice = 0
for i in num:
    print("O " + ordinais[indice] + " dígito é " + i)
    indice = indice + 1