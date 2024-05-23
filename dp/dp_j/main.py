N = int(input())
a = tuple(map(int, input().split()))

c = [0, 0, 0]
for ai in a:
    if ai > 0:
        c[ai - 1] += 1
# dp[i][j][k] := 寿司が残り1つの皿i枚, 2つの皿j枚, 3つの皿k枚としたとき、1つ寿司が減る期待値

dp = [
    [[0.0 for i in range(N + 2)] for j in range(N + 2)] for k in range(N + 2)
]
for k in range(N + 1):
    for j in range(N + 1):
        for i in range(N + 1):
            s = i + j + k
            if s:
                dp[i][j][k] = (
                    N
                    + i * dp[i - 1][j][k]
                    + j * dp[i + 1][j - 1][k]
                    + k * dp[i][j + 1][k - 1]
                ) / s

print(dp[c[0]][c[1]][c[2]])
# def rec(i, j, k):
#     if j > 0:
#         return dp[i][j][k] + rec(i + 1, j - 1, k)
#     if k > 0:
#         return dp[i][j][k] + rec(i, j + 1, k - 1)
#     return dp[i][j][k]

# print(count, rec(*count))
# for i in range(N + 1):
#     for j in range(N + 1 - i):
#         for k in range(N + 1 - i - j):
#             print(i, j, k, dp[i][j][k])
