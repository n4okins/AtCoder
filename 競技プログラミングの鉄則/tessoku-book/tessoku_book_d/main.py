"""
Title: A04 - Binary Representation 1
URL: https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_d

Question:

整数 N が 10 進法表記で与えられます。
N を 2 進法に変換した値を出力するプログラムを作成してください。

Rule:

N は 1 以上 1000 以下の整数

"""

N = int(input())
s = ""
while N >= 1:
    s = str(N % 2) + s
    N = N // 2
print(f"{s:>010}")