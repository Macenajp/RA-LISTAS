c = 1
s = 0
c1 = 0
c2 = 0

while c <= 20:
    if c % 3 == 0:
        s += c2
        c1 += 1
    elif c % 2 == 0:
        c2 += 1
    c += 1
print(s, c1, c2)
