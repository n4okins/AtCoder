"""
Title: A06 - How Many Guests?
URL: https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_ai

Question:
遊園地「ALGO-RESORT」では N 日間にわたるイベントが開催され、 i 日目 (1 \leq i
\leq N) には A_i 人が来場しました。
以下の合計 Q 個の質問に答えるプログラムを作成してください。

1 個目の質問：L_1 日目から R_1 日目までの合計来場者数は？
2 個目の質問：L_2 日目から R_2 日目までの合計来場者数は？
:
Q 個目の質問：L_Q 日目から R_Q 日目までの合計来場者数は？


Rule:
1 \le N,Q \le 10^5
1 \le A_i \le 10000
1 \le L_i \le R_i \le N
入力はすべて整数

"""

N, Q = map(int, input().split())
A = list(map(int, input().split()))

for i in range(1, len(A)):
    A[i] += A[i - 1]

for i in range(Q):
    Li, Ri = map(int, input().split())
    print(A[Ri - 1] - (A[Li - 2] if Li >= 2 else 0))