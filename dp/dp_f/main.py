# 最大の共通部分の長さ
# 最長共通部分列問題 (LCS)

s = input()
t = input()

dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

for si in range(len(s)):
    for ti in range(len(t)):
        if s[si] == t[ti]:
            dp[si + 1][ti + 1] = max(dp[si + 1][ti + 1], dp[si][ti] + 1)
        dp[si + 1][ti + 1] = max(dp[si + 1][ti + 1], dp[si + 1][ti], dp[si][ti + 1])


result = ""
si, ti = len(s), len(t)
while si > 0 and ti > 0:
    if s[si - 1] == t[ti - 1]:
        result += s[si - 1]
        si -= 1
        ti -= 1
    elif dp[si][ti - 1] > dp[si - 1][ti]:
        ti -= 1
    else:
        si -= 1

print(result[::-1])
