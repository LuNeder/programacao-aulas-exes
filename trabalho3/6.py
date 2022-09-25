n = float(input())
j = n
i = 0
s = 0

while j > 0:
    s = s + ((i+1)/j)
    i = i + 1
    j = n - i
    
print("%.48f" % s)