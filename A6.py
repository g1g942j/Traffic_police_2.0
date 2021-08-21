season = {'1':'Зима','2':'Зима','3':'Весна','4':'Весна','5':'Весна','6':'Лето','7':'Лето','8':'Лето','9':'Осень','10':'Осень','11':'Осень','12':'Зима',}
x = input()
print(season.get(x))


def mirror(st):
    long = len(st)
    y = long-1
    for i in long:
        print(st[y])
        y = y-1


from collections import Counter
list1 = ['Яблоко', 'Груша', 'Слива', 'Персик']
list2 = ['666', '1', 'Отсутствует', '834']



lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
x = int(input())
if x == 1:
    for p in lst:
        if p%3 == 0:
            print(p)
elif x == 2:
    for u in lst:
        if u<30 and u%2==0:
            print(u)

x = input()
summa = 0
lf = len(x)
x = int(x)
while True:
    t = x%10
    x = x//10
    summa += x
    print(summa)
    lf = lf - 1
    if lf == 0:
        break
        print(summa)

x = input()
z = len(x)
i = 0
f = z-1
if z%2 ==0:
    while True:
        if x[i] != x[f]:
            print("Нет")
            break
        else:
            i +=1
            f-=1
            if i == z:
                print("Да")
                break
else:
    while True:
        if x[i] != x[f]:
            print("Нет")
            break
        else:
            i +=1
            f-=1
            if i == z:
                print("Да")
                break