"""
Title: A05 - Three Cards
URL: https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_e

Question:

赤・青・白の 3 枚のカードがあります。
太郎君は、それぞれのカードに 1 以上 N 以下の整数を書かなければなりません。
3 枚のカードの合計を K にするような書き方は何通りありますか。

Rule:

N は 1 以上 3000 以下の整数
K は 3 以上 9000 以下の整数

"""
N, K = map(int, input().split())
count = 0
for n in range(1, N + 1):
    for m in range(1, N + 1):
        if 0 < K - (n + m) <= N:
            count += 1

print(count)