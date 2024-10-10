b = [input().strip() for _ in range(3)]
result = '?'

for i in range(3):
    if b[i][0] == b[i][1] == b[i][2] and b[i][0] in 'X0':
        result = b[i][0]

for i in range(3):
    if b[0][i] == b[1][i] == b[2][i] and b[0][i] in 'X0':
        result = b[0][i]

if b[0][0] == b[1][1] == b[2][2] and b[0][0] in 'X0':
    result = b[0][0]
if b[0][2] == b[1][1] == b[2][0] and b[0][2] in 'X0':
    result = b[0][2]

print(result)
