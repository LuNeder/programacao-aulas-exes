m, a = input().split()

imc = (float(m)/ (float(a)**2))
print("%.2f" % imc)
if imc < 18.5:
    print("abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("saudável")
elif imc >=  25 and imc <= 29.9:
    print("sobrepeso")
elif imc >= 30 and imc <= 34.9:
    print("obesidade grau 1")
elif imc >= 35 and imc <= 39.9:
    print("obesidade severa")
else:
    print("obesidade mórbida")
