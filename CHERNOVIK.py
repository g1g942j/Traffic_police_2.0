for line in file:
    l = len(line)
    i = 0
    while True:
        s = line[i]
        stroka = s
        if stroka == ':':
            f1.append(stroka1)
        else:
            stroka1 = stroka1 + stroka
            stroka = ''
            i += 1
        if i == l:
            break
    while True:
        if stroka == ' ':
            f2.append(stroka3)
            break
        else:
            stroka2 = stroka2 + stroka
            stroka = ''
            i += 1
        if i == l:
            break
print(f1)
print(f2)







for lin in file:
    s = lin[i]
    l = len(lin)
    while True:
        if s == ':':
            i += 1
            break
        i += 1
    while True:
        print(q)
        s = lin[i]
        l = len(lin)
        if s == ' ':
            f2.append(stroka1)
            stroka1 = ''
            i = q
            break
        stroka1 = stroka1 + s
        i += 1
        if i == l:
            i = q
            stroka1 = ''
            break
        print(f2)
