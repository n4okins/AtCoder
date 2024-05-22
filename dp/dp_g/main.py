import sys

sys.setrecursionlimit(1024**2)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
d = [-1] * (N)
for i in range(M):
    x, y = map(int, input().split())
    G[x - 1].append(y - 1)


def rec(v):
    if d[v] != -1:
        return d[v]
    global max_res
    res = 0
    for nv in G[v]:
        res = max(res, rec(nv) + 1)
    d[v] = res
    return res


for n in range(N):
    rec(n)
print(max(d))
