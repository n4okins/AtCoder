N = int(input())
h = list(map(int, input().split()))


# 緩和処理を行う
def chmin(a, b):
    if a > b:
        a = b
    return a


INF = 1 << 60
dp = [INF] * N
dp[0] = 0  # 初期条件

for i in range(N):
    if (i + 1 < N):
        dp[i + 1] = chmin(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]))
    if (i + 2 < N):
        dp[i + 2] = chmin(dp[i + 2], dp[i] + abs(h[i] - h[i + 2]))

print(dp[N - 1])
