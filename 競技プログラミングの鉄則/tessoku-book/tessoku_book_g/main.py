"""
Title: A07 - Event Attendance
URL: https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_g

Question:

ある会社では D 日間にわたってイベントが開催され，N 人が出席します．参加者 i は
L_i 日目から R_i 日目まで出席する予定です．
各日の出席者数を出力するプログラムを作成してください．

Rule:

1\leq D,N\leq 10^5
1\leq L_i\leq R_i\leq D
入力はすべて整数

"""

D = int(input())
N = int(input())
data = [0] * (D + 2)
L, R = [0] * N, [0] * N

for i in range(N):
    L[i], R[i] = map(int, input().split())

for i in range(N):
    data[L[i]] += 1
    data[R[i] + 1] -= 1

for i in range(1, D + 1):
    data[i] = max(0, data[i] + data[i - 1])

for d in data[1:-1]:
    print(d)
