val = int(input())

def caixa_eletronico(val):
    
    notas = {}
    #100, 50, 20, 10, 5, 2
    notas[100] = val // 100
    f =  (val % 100)
    notas[50] = f // 50
    f =  (f % 50)
    notas[20] = f // 20
    f =  (f % 20)
    notas[10] = f // 10
    f =  (f % 10)
    notas[5] = f // 5
    f =  (f % 5)
    notas[2] = f // 2
 

    return notas


print(caixa_eletronico(val))