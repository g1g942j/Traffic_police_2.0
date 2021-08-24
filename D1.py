import collections
st = 'pythonist'
ls = []
lt = []
l = len(st)
i = 0
while True:
    s = st[i]
    ls.append(s)
    i += 1
    if l == i:
        lt = ls
        print(ls)
        break
lt = sorted(lt)
print(collections.Counter(st))
file = open('/home/user/gym-duckietown/file.txt', 'r')
stroka = ''
stroka0 = ''
stroka1 = ''
f1 = []
f2 = []
i = 0
q = 0
for line in file:
    if len(line) == 1:
        continue
    while True:
        s = line[i]
        l = len(line)
        if s == ':':
            f1.append(stroka)
            stroka = ''
            i = 0
            break
        stroka = stroka + s
        i += 1
        if i == l:
            i = 0
            stroka = ''
            break
        q += 1
print(f1)
f = open('/home/user/gym-duckietown/file.txt', 'r')
print(f1)
fn2 = []
fn3 = []
for lk in f:
    if len(lk) == 1:
        continue
    if len(lk) == 0:
        continue
    lk = lk.split(':')
    #print(lk)
    #print(lk[1])
    s = lk[1][:-1]
    fn3.append(s)
fns = dict(zip(f1, fn3))
print(fns)