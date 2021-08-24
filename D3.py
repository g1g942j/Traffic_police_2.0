f = open('/home/user/gym-duckietown/file.txt', 'r')
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

    fn2.append(s)
print(fn2)