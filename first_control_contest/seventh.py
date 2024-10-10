def clean(input_string):
    return set(input_string.replace('+7', '8')
               .replace('(', '').replace(')', '')
               .replace('-', '').replace(' ', '')
               .split(', '))


source_a = clean(input())
source_b = clean(input())
source_c = clean(input())
exceptions = clean(input())
number_to_check = (input().replace('+7', '8')
                   .replace('(', '').replace(')', '')
                   .replace('-', '').replace(' ', ''))

source_A = []
source_B = []
source_C = []
Exceptions = []
for i in range(len(str(source_a).split(','))):
    if i == 0:
        source_A.append(str(source_a).split(',')[i][2:])
    elif i == len(str(source_a).split(',')) - 1:
        source_A.append(str(source_a).split(',')[i][:-2])
    else:
        source_A.append(str(source_a).split(',')[i])
for i in range(len(str(source_b).split(','))):
    if i == 0:
        source_B.append(str(source_b).split(',')[i][2:])
    elif i == len(str(source_b).split(',')) - 1:
        source_B.append(str(source_b).split(',')[i][:-2])
    else:
        source_B.append(str(source_b).split(',')[i])
for i in range(len(str(source_c).split(','))):
    if i == 0:
        source_C.append(str(source_c).split(',')[i][2:])
    elif i == len(str(source_c).split(',')) - 1:
        source_C.append(str(source_c).split(',')[i][:-2])
    else:
        source_C.append(str(source_c).split(',')[i])
for i in range(len(str(exceptions).split(','))):
    if i == 0:
        Exceptions.append(str(exceptions).split(',')[i][2:])
    elif i == len(str(exceptions).split(',')) - 1:
        Exceptions.append(str(exceptions).split(',')[i][:-2])
    else:
        Exceptions.append(str(exceptions).split(',')[i])

flag = (number_to_check in source_A) + (number_to_check in source_B) + (number_to_check in source_C)

if number_to_check in Exceptions or flag < 2:
    print("NOT SPAM")
else:
    print("SPAM")
