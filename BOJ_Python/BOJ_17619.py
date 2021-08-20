# 개구리 점프
import sys
input = sys.stdin.readline
print = sys.stdout.write

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, Q = map(int, input().split())
parent = [0] + [i for i in range(1, N+1)]
wood = []
for v in range(1, N+1):
    x1, x2, y = map(int, input().split())
    wood.append((x1, x2, y, v))
wood.sort(key=lambda x:x[0])
wood_start, wood_end, tmp, wood_v = wood[0]
for i in range(1, N):
    start, end, t, wv = wood[i]
    if wood_end >= start:
        wood_end = max(wood_end, end)
        union(wood[i-1][3], wv)
    else:
        wood_start, wood_end = start, end
for _ in range(Q):
    u, v = map(int, input().split())
    if find(u) == find(v):
        print('1'+'\n')
    else:
        print('0'+'\n')