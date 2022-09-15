num = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"]
dez = ["zerenta", "dezeta", "vinte", "trinta", "quarenta"]
fsl = []
input = input()
for i in input:
    fsl.append(i)

try:
    f, s = fsl
    double = True
except:
    double = False
    s = "0"
    f = int(fsl[0])



if "0" in s:
    e = ""
else:
    e = " e "

# print(e)
s = int(s)
if double == False:
    print(num[int(f)])
elif int(input) <= 19:
    print(num[int(input)])
elif num[int(s)] == "zero":
    print(dez[int(f)])
else:
    print(dez[int(f)] + e + num[int(s)])
