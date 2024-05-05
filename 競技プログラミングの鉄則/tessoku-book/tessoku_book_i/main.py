"""
Title: A09 - Winter in ALGO Kingdom
URL: https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_i

Question:

ALGO 王国は H\times W のマス目で表されます．最初は，どのマスにも雪が積もっていま
せんが，これから N 日間にわたって雪が降り続けます．
上から i 行目，左から j 列目のマスを (i, j) とするとき，t 日目には
「マス (A_t, B_t) を左上とし，マス (C_t, D_t) を右下とする長方形領域」の積雪が
1cm だけ増加することが予想されています．
最終的な各マスの積雪を出力するプログラムを作成してください．

Rule:

1\leq H,W\leq 1500
1\leq N\leq 100000
1\leq A_i\leq C_i\leq H
1\leq B_i\leq D_i\leq W
入力はすべて整数
"""

H, W, N = map(int, input().split())
ALGO = [[0] * (W + 1) for _ in range(H + 1)]

for n in range(N):
    A, B, C, D = map(int, input().split())
    ALGO[A - 1][B - 1] += 1
    ALGO[A - 1][D] -= 1
    ALGO[C][B - 1] -= 1
    ALGO[C][D] += 1

for h in range(H):
    for w in range(1, W):
        ALGO[h][w] += ALGO[h][w - 1]

for w in range(W):
    for h in range(1, H):
        ALGO[h][w] += ALGO[h - 1][w]

for r in ALGO[:-1]:
    print(*r[:-1])