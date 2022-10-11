tab = []

# coluna vai ser linha (transposta)
for i in range(0, 7):
    c = []
    for j in range(0, 6):
       c.append(0)
    tab.append(c) 

print(tab)





def jogada(jog, lug):
    for i in reversed(range(0, len(tab[lug]))):
        if tab[lug][i] == 0:
            tab[lug][i] = jog
            print(tab)
            return "done"




def check():
    print()



while True:
    jog1 = int(input())
    jogada(1, jog1)
    check()


    jog2 = int(input())
    jogada(2, jog2)
    check()