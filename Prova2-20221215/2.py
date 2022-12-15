def traducao_rna(i, o):
    import re
    import os
    i = open(i, "r")
    i = i.read()
    trinca = re.findall("...", i)
    amino = []

    for i in trinca:
        a = i.replace("UUU", "Phe ")
        a = a.replace("CUU", "Leu ")
        a = a.replace("UUA", "Leu ")
        a = a.replace("AAG", "Lis ")
        a = a.replace("UCU", "Ser ")
        a = a.replace("UAU", "Tyr ")
        a = a.replace("CAA", "Gln ")
        amino.append(a)
    
    s = ""

    for i in amino:
        s = s + i
    
    s = s.strip()
    s = s.replace(" ", "-")

    o = open(o, "w")
    o.write(s)

