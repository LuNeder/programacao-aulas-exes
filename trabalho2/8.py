cv, ce, cs = input().split()
fv, fe, fs = input().split()

cv = int(cv); ce = int(ce); cs = int(cs)
fv = int(fv); fe = int(fe); fs = int(fs)

fp = (fv * 3) + fe
cop = (cv *3) + ce

if fp > cop:
    print("Flamengo")
elif cop > fp:
    print("Corinthians")
elif cs > fs:
    print("Corinthians")
elif fs > cs:
    print("Flamengo")
else:
    print("Empate")