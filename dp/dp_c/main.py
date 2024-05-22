N = int(input())
act = {k: [0] * N for k in "ABC"}
dp = {k: [0] * N for k in "ABC"}

for i in range(N):
    act["A"][i], act["B"][i], act["C"][i] = map(int, input().split())
    if i == 0:
        dp["A"][0], dp["B"][0], dp["C"][0] = act["A"][0], act["B"][0], act["C"][0]


# N はたかだか10^5
for i in range(1, N):  # i日目について
    for k in "ABC":  # A, B, Cの行動のいずれかを取る
        for t in "ABC".replace(
            k, ""
        ):  # 一つ前の日の行動がどれか, 連続して同じ行動はとれない
            # すでに求めた値か、一つ前の行動と今取る行動の合計値のうち大きい方を記録
            dp[k][i] = max(dp[k][i], dp[t][i - 1] + act[k][i])


print(max(sum(dp.values(), [])))
