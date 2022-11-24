def dataine(data):
    pass

def datainb(data):
    d = [int(x) for x in data.split("/")]
    ltime = d[0]
    dmonth = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    i = d[1]
    while i > 0:
        ltime = ltime + dmonth[d[1]-i]
        i -= 1
    return ltime

def esta(lt):
    if 265 <= lt <= 355:
        return "Primavera"
    elif lt >= 356 or lt <= 80:
        return "Verão"
    elif 81 <= lt <= 172:
        return "Outono"
    elif 173 <= lt <= 264:
        return "Inverno"


def estacao_do_ano(data):
    if "/" in data:
        ltime = datainb(data)
        return esta(ltime)
    elif " " in data:
        ltime = dtaine(data)
        return esta(ltime)
    else:
        exit(9)


while True:
    data = input()
    if data=='-1':
        exit(0)
    else:                
        print(estacao_do_ano(data))