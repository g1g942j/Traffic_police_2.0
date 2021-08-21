s = 'f4jv )(*vn4'
print(s[2])
print(s[-1])
print(len(s))
x = input()
if x[0] == 'a':
    print("Yes")
else:
    print("No")
s = input()
if s[0] == 'a' and len(s) <= 10 and s[-1].isalpha() == True:
    print('Yes')
else:
    print("No")

# count, replace, find, rfind