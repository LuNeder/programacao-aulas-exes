
def converte(horario):
    vqh = [int(x) for x in horario.split(':')]
    if int(vqh[0]) < 12:
        am = "A.M"
        hh = vqh[0]
    elif int(vqh[0]) == 12:
        am = "P.M"
        hh = vqh[0]
    elif int(vqh[0]) > 12:
        am = "P.M"
        hh = vqh[0] - 12
    else:
        exit(9)

    if len(str(hh)) == 1:
        hh = "0" + str(hh)
    if len(str(vqh[1])) == 1:
        vqh[1] = "0" + str(vqh[1])
    if hh == "00":
        hh = "12"

    dzh = [hh, vqh[1]]
    return str(dzh[0]) + ":" + str(dzh[1]) + " " + am

while True:
    horario = input()
    if horario=='-1':
        break
    else:
        print(converte(horario))