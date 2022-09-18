ano = int(input())

q = ano % 4
d = ano % 100
qq = ano % 400

if q == 0:
    if d == 0:
        nada = 0
    else:
        print("SIM")
        exit(0)

if qq == 0:
    print("SIM")
    exit(0)

print("NÃO")