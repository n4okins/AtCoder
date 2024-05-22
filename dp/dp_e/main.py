N, W = map(int, input().split())
w, v = [0] * N, [0] * N
for i in range(N):
    w[i], v[i] = map(int, input().split())

sum_v = sum(v)
sum_w = sum(w)
# 制約があるので、固定された重さの中で価値を最大化するのではなく
# 固定された価値の中で重さを最小化する問題として考える
# 最大の重さの合計値まで調べれば良いので, 0 ~ sum_vが調べられるようにする
# つまりsum_v + 1まで必要
# 重さの最大値はsum_wなのでわざわざINF使うな
dp = [[sum_w] * (sum_v + 1) for _ in range(N + 1)]

# dp[i][weight]: min_weight

dp[0][0] = 0

for i in range(N):
    for target_sum_value in range(sum_v + 1):
        if target_sum_value - v[i] >= 0:
            dp[i + 1][target_sum_value] = min(
                dp[i + 1][target_sum_value], dp[i][target_sum_value - v[i]] + w[i]
            )
        dp[i + 1][target_sum_value] = min(
            dp[i + 1][target_sum_value], dp[i][target_sum_value]
        )

res = 0

for target_sum_value in range(sum_v + 1):
    if dp[N][target_sum_value] <= W:
        res = target_sum_value

print(res)
