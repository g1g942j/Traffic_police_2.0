def mirror(st):
    x = len(st)
    while True:
        x = x-1
        print(st[x])
        if x == 0:
            break
x = input()
mirror(x)

list1 = ['Яблоко', 'Груша', 'Слива', 'Персик']
list2 = ['666', '1', 'Отсутствует', '834']
d = dict(zip(list1, list2))
print(d)

