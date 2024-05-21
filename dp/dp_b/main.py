N, K = map(int, input().split())
h = tuple(map(int, input().split()))

INF = 1 << 60
dp = [INF] * N


"""
dp[i] ← 足場iにおける、足場1からの最小コスト
"""

dp[0] = 0
for i in range(N):
    for j in range(1, K + 1):
        if i + j < N:
            # ジャンプ先が存在するなら
            # i + j 番目は現時点でのコストか、それより小さくなるか
            dp[i + j] = min(dp[i + j], dp[i] + abs(h[i + j] - h[i]))

print(dp[N - 1])
