a = int(input())

if a == 0:
    print("verde")
elif (1 <= a <= 10) and a % 2 == 0:
    print("preto")
elif (1 <= a <= 10) and a % 2 != 0:
    print("vermelho")
elif (11 <= a <= 18) and a % 2 == 0:
    print("vermelho")
elif (11 <= a <= 18) and a % 2 != 0:
    print("preto")
elif (19 <= a <= 28) and a % 2 == 0:
    print("preto")
elif (19 <= a <= 28) and a % 2 != 0:
    print("vermelho")
elif (29 <= a <= 36) and a % 2 == 0:
    print("vermelho")
elif (29 <= a <= 36) and a % 2 != 0:
    print("preto")
else:
    print("entrada inválida")