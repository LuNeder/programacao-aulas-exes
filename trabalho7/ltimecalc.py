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


def estacao_do_ano(data):
    if "/" in data:
        return datainb(data)
    elif " " in data:
        return dtaine(data)
    else:
        exit(9)


while True:
    data = input()
    if data=='-1':
        exit(0)
    else:                
        print(estacao_do_ano(data)) 