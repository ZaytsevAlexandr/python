import math


f = open(str(input()), 'r', encoding='utf-8')
a = f.read().splitlines()
f.close()

name = []
mark = []
failed = 0
for i in a:
    m = i.split(';')
    name.append(m[0])
    mark.append(m[1])

for m in mark:
    if m <= '2' or m == 'Н':
        failed += 1

print(math.floor(failed / len(name) * 100))
# except:
#    print('no data')



