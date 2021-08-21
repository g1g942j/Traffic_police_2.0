st = "1, 2, 3, 4, 5, 6, a, 8, 9, 0"
counter = 0
for i in st:
    if i.isdigit() == True:
        counter += 1
print(counter)

x = input()
summa_1 = int(x[0]) + int(x[1]) + int(x[2])
summa_2 = int(x[-1]) + int(x[-2]) + int(x[-3])
if summa_1 == summa_2:
    print("Счастливый")
else:
    print('Не счастливый')

l = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
lt = []
lt.append(l[2])
lt.append(l[4])
lt.append(l[6])
lt.append(l[8])
print(','.join(lt))

while True:
    x = int(input())
    if x > 100:
        break
    elif x < 10:
        continue
    else:
        print(x)


