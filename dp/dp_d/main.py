N, W = map(int, input().split())
w, v = [0] * N, [0] * N
for i in range(N):
    w[i], v[i] = map(int, input().split())

dp = [[0] * (W + 1) for _ in range(N + 1)]

# dp[i][weight]: max_value


for i in range(N):
    for weight in range(W + 1):
        # 重さを固定し、i番目の品物を選ぶ
        if weight - w[i] >= 0:
            # 重さに余裕があるならば（i番目を選べるならば）
            # すでに求めた値と、一つ前から余裕のある重さ分(weight - w[i])の最大値に新たなv[i]を追加した値で比較
            dp[i + 1][weight] = max(dp[i + 1][weight], dp[i][weight - w[i]] + v[i])

        # 余裕があってもなくても一つ上（i番目の品物を選ばなかった場合）と比較しておく
        dp[i + 1][weight] = max(dp[i + 1][weight], dp[i][weight])

print(dp[N][W])
