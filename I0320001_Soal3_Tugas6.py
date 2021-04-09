# Penentu Bilangan Prima
x = 1
y = 30

for z in range(x, y + 1):
    if z == 1:
        print(z,"bukan prima")
    elif z == 2:
        print(z,"bukan prima")
    elif z > 1:
        for i in range(2, z):
            if (z % i) == 0:
                print(z, "bukan prima")
                break
    else:
        print(z, "bilangan prima")