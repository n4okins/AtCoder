"""
Title: A11 - Binary Search 1
URL: https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_k

Question:

小さい順に並べられている、要素数 N の配列 A = [A_1, A_2, \cdots, A_N] がありま
す。要素 X は配列 A の何番目に存在するかを出力してください。
なお、この問題は単純な全探索（→1.2節）でも解けますが、ここでは二分探索法を使って
実装してください。

Rule:

1 \leq N \leq 100000
1 \leq A_1 < A_2 < \cdots < A_N \leq 10^9
整数 X は A_1, A_2, \ldots, A_N のいずれかである

"""
N, X = map(int, input().split())
A = tuple(map(int, input().split()))

def binary_search(li, ri, array = A, target = X):
    m = (li + ri) // 2
    if target == array[m]:
        return m + 1
    elif target < array[m]:
        return binary_search(li, m - 1, array, target)
    elif array[m] < target:
        return binary_search(m + 1, ri, array, target)

print(binary_search(0, len(A) - 1))
