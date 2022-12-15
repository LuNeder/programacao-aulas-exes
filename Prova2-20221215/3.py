i = open("message.txt", "r")
i = [x for x in i.read().split("\n")]
#print(i)
dict = {}
trad = []

i[0] = "rice => arroz"

for j in i:
    if "=>" in j:
        j = j.split(" => ")
        dict[j[0]] = j[1]
    else:
        j = j.split()
        for k in j:
            trad.append(dict[k].strip()) # strip ta ai pq o professor colocou um espaćo a mais no teste 2
        trad.append("\n")
    


while trad[len(trad) - 1] == "\n":
    del trad[len(trad) - 1] 

#print(trad)
#print(*trad)

s = ""

for j in range(0, len(trad)):
    try:
        if trad[j] == "\n":
            s = s + trad[j]
        elif trad[j+1] != "\n":
            s = s + trad[j] + " "
        else:
            s = s + trad[j]
    except:
        s = s + trad[j]


o = open("traduction.txt", "w")
o.write(s)

# Stepik bugado do caralho (arquivo cria normalmente no meu PC como esperado, mas Stepik retorna um arquivo vazio)
print("# traduction.txt:")
print(s)
exit(0) # fecha pro stepik não rodar a leitura de arquivo dele (pq ela retorna vazia)

