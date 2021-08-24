file = open('/home/user/gym-duckietown/file.txt', 'r')
stroka = ''
stroka0 = ''
stroka1 = ''
f1 = []
f2 = []
i = 0
q = 0

for lin in file:
    while True:
        s = lin[i]
        print(s)
        l = len(lin)
        if s == ' ':
            i = i-1
            s = lin[i]
            print(s)
        if s == ':':
            f2.append(stroka1)
            stroka1 = ''
            i = -1
            break
        stroka1 = stroka1 + s
        i -= 1
        if i == l:
            i = -1
            stroka1 = ''
            break
        q += 1
        print(f2)

