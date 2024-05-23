H, W = map(int, input().split())
a = tuple([tuple(input()) for _ in range(H)])


M = 10**9 + 7

# dp[i][j] ← (i, j)における経路数
dp = [[0] * W for _ in range(H)]

dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if i >= 1:
            if a[i][j] == ".":
                dp[i][j] += dp[i - 1][j]
        if j >= 1:
            if a[i][j] == ".":
                dp[i][j] += dp[i][j - 1]

print(dp[H - 1][W - 1] % M)
