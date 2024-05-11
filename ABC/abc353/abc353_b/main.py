N, K = map(int, input().split())
A = tuple(map(int, input().split()))
k = K
cnt = 1
for Ai in A:
    if k < Ai:
        cnt += 1
        k = K - Ai
    else:
        k -= Ai

print(cnt)
