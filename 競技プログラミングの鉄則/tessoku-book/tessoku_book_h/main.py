"""
Title: A08 - Two Dimensional Sum
URL: https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_h

Question:

H\times W のマス目があります．上から i 行目，左から j 列目にあるマス (i, j) に
は，整数 X_{i, j} が書かれています．
これについて，以下の Q 個の質問に答えるプログラムを作成してください．

i 個目の質問：左上 (A_i, B_i) 右下 (C_i, D_i) の長方形領域に書かれた整数の総
和は？


Rule:

1\leq H,W\leq 1500
1\leq Q\leq 100000
0\leq X_{i,j}\leq 9
1\leq A_i\leq C_i\leq H
1\leq B_i\leq D_i\leq W
入力はすべて整数
"""

H, W = map(int, input().split())
X = [[0] * (W + 1) for _ in range(H + 1)]
for h in range(H):
    X[h + 1][1:] = list(map(int, input().split()))

Q = int(input())

for i in range(H + 1):
    for j in range(1, W + 1):
        X[i][j] += X[i][j - 1]

for j in range(W + 1):
    for i in range(1, H + 1):
        X[i][j] += X[i - 1][j]

for q in range(Q):
    A, B, C, D = map(int, input().split())
    print(X[A - 1][B - 1] + X[C][D] - X[A - 1][D] - X[C][B - 1])