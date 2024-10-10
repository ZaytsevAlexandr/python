N, K, M = map(int, input().split())
D_m = list(map(int, input().split()))

for i in range(M):
    N = N - D_m[i]
    if N < 0 or N == 0:
        N = 0
        break
    N += D_m[i] * K

print(N)
