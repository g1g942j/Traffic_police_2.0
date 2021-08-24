from collections import Counter
st = 2345067899
st = str(st)
x = Counter(st)
print(x)
b = 0
i = 0
for i in range(10):
    f = i
    f = str(f)
    results = x.get(i)
    if results != 0:
        b = 0
        print('NO{}'.format(results))

if b == 0:
    print('Yes')