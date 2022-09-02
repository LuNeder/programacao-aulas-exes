h, m, ss = input().split(":")

hs = float(h) * 60 * 60
ms = float(m) * 60
ss = float(ss)

print( int(hs + ms + ss))