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