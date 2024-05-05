"""
Title: A13 - Close Pairs
URL: https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_m

Question:

N 個の整数が黒板に書かれています。書かれた整数は小さい順に A_1, A_2, \cdots, A_N
です。異なる 2 つの整数のペアを選ぶ方法は全部で N(N-1)/2 通りありますが、その中
で差が K 以下であるような選び方は何通りありますか。

Rule:

1 \leq N \leq 100\,000
1 \leq K \leq 10^9
1 \leq A_1 < A_2 < \cdots < A_N \leq 10^9
入力はすべて整数

"""
N, K = map(int, input().split())
A = tuple(map(int, input().split()))

i = 0
cnt = 0

while i < N:
    for j in range(i + 1, N):
        if A[j] - A[i] <= K:
            cnt += 1
        else:
            i = j
            break
    else:
        break
print(cnt)