"""
Title: A10 - Resort Hotel
URL: https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_j

Question:

あるリゾートホテルには，1 号室から N 号室までの N 個の部屋があります．
i 号室は A_i 人部屋です．このホテルでは D 日間にわたって工事が行われることになっ
ており，
d 日目は L_d 号室から R_d 号室までの範囲を使うことができません．
d=1,2,\cdots D について，d 日目に使える中で最も大きい部屋は何人部屋であるか，出
力するプログラムを作成してください．

Rule:

3\leq N\leq 100000
1\leq D\leq 100000
1\leq A_i\leq 100
2\leq L_i\leq R_i\leq N - 1
入力はすべて整数
"""
N = int(input())
A = list(map(int, input().split()))
D = int(input())

LAmax = [0] * N
RAmax = [0] * N

LAmax[0] = A[0]
RAmax[0] = A[-1]

for n in range(1, N):
    LAmax[n] = max(LAmax[n - 1], A[n])
    RAmax[n] = max(RAmax[n - 1], A[- n - 1])

LAmax = [0] + LAmax
RAmax = list(reversed(RAmax)) + [0]

for d in range(D):
    Ld, Rd = map(int, input().split())
    print(max(LAmax[Ld - 1], RAmax[Rd]))


