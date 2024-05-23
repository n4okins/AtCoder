N, K = map(int, input().split())
a = tuple(map(int, input().split()))

# dp[i] := 石の個数残りi個の局面で、勝ちか負けか

dp = [False for i in range(K + 1)]

for i in range(1, K + 1):
    for j in range(N):
        if i - a[j] >= 0:
            dp[i] |= not dp[i - a[j]]

print("First" if dp[K] else "Second")