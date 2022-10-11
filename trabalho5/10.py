tab = []

# coluna vai ser linha (transposta)
for i in range(0, 7):
    c = []
    for j in range(0, 6):
       c.append(0)
    tab.append(c) 

print(tab)





def fim(ganhador):
    print("Jodador " + ganhador + "Venceu!")


def jogada(jog, lug):
    for i in reversed(range(0, len(tab[lug]))):
        if tab[lug][i] == 0:
            tab[lug][i] = jog
            success = [lug, i]
            print(tab)
            return success




def check(casa, ganhador):
    c = casa[0]
    l = casa[1]
    test = tab[c][l]
    
    # DIREITA
    try:
        if test == tab[c+1][l]: 
            if test == tab[c+2][l]:
                if test == tab[c+3][l]:
                    fim(ganhador)
    except:
        a = "a"

    # ESQUERDA
    try:
        if test == tab[c-1][l]:
            if test == tab[c-2][l]:
                if test == tab[c-3][l]:
                    fim(ganhador)
    except:
        a = "a"


    # CIMA
    try:
        if test == tab[c][l+1]:
            if test == tab[c][l+2]:
                if test == tab[c][l+3]:
                    fim(ganhador)
    except:
        a = "a"
   

    # BAIXO
    try:
        if test == tab[c][l-1]:
            if test == tab[c][l-2]:
                if test == tab[c][l-3]:
                    fim(ganhador)
    except:
        a = "a"


    # DIAGONAL cima-direita
    try:
        if test == tab[c+1][l+1]:
            if test == tab[c+2][l+2]:
                if test == tab[c+3][l+3]:
                    fim(ganhador)
    except:
        a = "a"


    # DIAGONAL baixo-direita
    try:
        if test == tab[c+1][l-1]:
            if test == tab[c+2][l-2]:
                if test == tab[c+3][l-3]:
                    fim(ganhador)
    except:
        a = "a"


    #DIAGONAL baixo-esquerda
    try:
        if test == tab[c-1][l-1]:
            if test == tab[c-2][l-2]:
                if test == tab[c-3][l-3]:
                    fim(ganhador)
    except:
        a = "a"


    #DIAGONAL cima-esquerda
    try:
        if test == tab[c-1][l+1]:
            if test == tab[c-2][l+2]:
                if test == tab[c-3][l+3]:
                    fim(ganhador)
    except:
        a = "a"






while True:
    jog1 = int(input())
    casa = jogada(1, jog1)
    check(casa, 1)


    jog2 = int(input())
    casa = jogada(2, jog2)
    check(casa, 2)