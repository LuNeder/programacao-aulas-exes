# Do enunciado: "...são chamadas de cores primárias porque não podem ser obtidas pela mistura de outras cores." Isso é mentira! 

c1 = input()
c2 = input()

cores = [c1, c2]

if "azul" in cores and c1 == c2:
    print("azul")
elif "amarelo" in cores and c1 == c2:
    print("amarelo")
elif "vermelho" in cores and c1 == c2:
    print("vermelho")
elif "azul" in cores and "vermelho" in cores:
    print("roxo")
elif "azul" in cores and "amarelo" in cores:
    print("verde")
elif "amarelo" in cores and "vermelho" in cores:
    print("laranja")
else:
    print("cores não primárias")
