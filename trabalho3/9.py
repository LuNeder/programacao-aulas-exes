n = int(input())
ph = []
l = {}

for i in range(0, n):
    ph.append(input())

test = input()

num = 0
for i in test:
    l[i] = 0
    for phrase in ph:
        for word in phrase:
            for letter in word:
                if i == letter:
                    l[i] = l[i] + 1

    print(i + " = " + str(l[i]))
    
