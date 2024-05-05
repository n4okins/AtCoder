"""
Title: A02 - Linear Search
URL: https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_b

Question:

N 個の整数 A_1, A_2, \cdots, A_N の中に、整数 X が含まれるかどうかを判定するプロ
グラムを作成してください。

Rule:

N は 1 以上 100 以下の整数
X は 1 以上 100 以下の整数
A_1, A_2, \cdots, A_N は 1 以上 100 以下の整数

"""
N, X = map(int, input().split())
A = map(int, input().split())
print("Yes" if X in A else "No")
