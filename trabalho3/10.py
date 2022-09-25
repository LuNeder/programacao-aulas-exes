valid = False

print("Informe uma nota entre 0 e 10!")

try:
    n = int(input())
    if 0 <= n <= 10:
        valid = True
    else:
        valid = False
except:
    valid = False


while valid == False:
    print("Nota inválida, digite uma nota entre 0 e 10!")
    try:
        n = int(input())
        if 0 <= n <= 10:
            valid = True
        else:
            valid = False

    except:
        valid = False




if valid == True:
    print("Nota válida!!!")
else:
    exit(4)

