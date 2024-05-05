"""
Title: A12 - Printer
URL: https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_l

Question:

N 台のプリンターがあり、1 から N までの番号が付けられています。プリンター i は
A_i 秒ごとにチラシを 1 枚印刷します。すなわち、スイッチを入れてから A_i 秒後、
2A_i 秒後、3A_i 秒後･･･ に印刷します。すべてのプリンターのスイッチを同時に入れた
とき、K 枚目のチラシが印刷されるのは何秒後でしょうか。

Rule:

1 \leq N \leq 100\,000
1 \leq K \leq 10^9
1 \leq A_i \leq 10^9
答えは 10^9 を超えない
入力はすべて整数
"""
N, K = map(int, input().split())
A = list(map(int, input().split()))

def printer(n):
    return sum(n // a for a in A)

def binary_search(ln, rn):
    while ln < rn:
        mn = (ln + rn) // 2
        if printer(mn) < K:
            ln = mn + 1
        else:
            rn = mn
    return ln

print(binary_search(1, 10 ** 9))