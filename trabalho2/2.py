claudio = int(input())

res = claudio % 2

if res == 0:
    print("Par")
else:
    print("Impar")

if claudio == 0:
    print("Zero")
elif claudio > 0:
    print("Positivo")
else:
    print("Negativo")
