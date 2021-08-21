x = input()
summa = 0
lf = len(x)-1
while True:
    z = int(x[lf])
    summa = summa + z
    lf -= 1
    if lf <0:
        print(summa)
        break