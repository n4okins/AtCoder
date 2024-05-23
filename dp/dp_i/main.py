N = int(input())
p = list(map(float, input().split()))

# dp[i][j]: i枚目まで投げたとき、表がj枚となる確率
dp = [[0.0] * (N + 1) for _ in range(N + 1)]

dp[0][0] = 1

for i in range(N):
    for j in range(i + 1):
        dp[i + 1][j + 1] += dp[i][j] * p[i]
        dp[i + 1][j] += dp[i][j] * (1 - p[i])

print(sum(dp[N][N // 2 + 1:]))
