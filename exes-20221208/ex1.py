def mult_matrizes(A, B, C):
    import numpy as np
    A = open(A, "r")
    B = open(B, "r")
    mA = A.read().split("\n")
    mB = B.read().split("\n")
    # dimA = [int(x) for x in mA[0].split()]
    # dimB = [int(x) for x in mB[0].split()]
    
    del mA[0]
    del mA[len(mA) - 1]
    del mB[0]
    del mB[len(mB) - 1]
    
    mmA = []
    mmB = []
    
    for i in range(len(mA)):
        mmA.append([float(x) for x in mA[i].split()])
        
    for i in range(len(mB)):
        mmB.append([float(x) for x in mB[i].split()])
    
    try:
        mmC = np.matmul(mmA, mmB)
    except:
        C = open(C, "w")
        C.write("Incompatíveis")
        return
    
    printC = []
    for i in mmC:
        #print(i)
        s = ""
        for k in range(0, len(i)):
            s += '%.2f ' % i[k]
        printC.append(s.strip())
        
    dimC = str(len(mmC)) + " " + str(len(mmC[0]))
    
    fC = open(C, "w")
    fC.write(dimC)
    fC.close()
    
    for i in printC:
        with open(C, "a") as Cc:
            Cc.write("\n" + i)
    
    