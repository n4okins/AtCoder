import numpy as np

M = pow(10, 8)


def f(x):
    return x % M


f = np.vectorize(f)
N = int(input())
A = np.asarray(list(map(int, input().split())))
i = 0
B = (A[i + 1 :] + A[i]) % M
print(B)
for i in range(1, N - 1):
    B[i:] += (A[i + 1 :] + A[i]) % M

print(np.sum(B))
