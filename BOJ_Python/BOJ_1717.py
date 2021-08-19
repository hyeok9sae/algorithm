# 집합의 표현
import sys
sys.setrecursionlimit(10**5)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(u, v):
    u, v = find(u), find(v)
    if u < v:
        parent[v] = u
    else:
        parent[u] = v

n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i
for _ in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        # if a == b:
        #     continue
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')