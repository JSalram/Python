from random import randint as r

for y in range(21):
    for x in range(21):
        qr = "■" if r(0, 1) else " "
        print(qr, end="")

    print()
