sx = input()
sn = input()
sd = input()

x = int(sx)
n = int(sn)
d = int(sd)

lst = list()
result = 1
x = x % d

if x == 0 and n == 0:
    print('0')
    quit()

while n >= 1:
    new = n % 2
    lst.append(new)
    n = int(n/2)

lst.reverse()
print(lst)

for i in lst:
    if i == 0:
        result = result * result
        if result > d:
            result = result % d
    else:
        result = result * result
        if result > d:
            result = result % d
        result = result * x
        if result > d:
            result = result % d
print(result)
