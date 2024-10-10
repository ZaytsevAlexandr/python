n, k = map(int, input().split())
m = [0] * n

for i in range(k):
    l, r = map(int, input().split())
    for j in range(l - 1, r):
        m[j] = 1

ans = sum(m)
print(n - ans)
