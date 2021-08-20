# 최소 스패닝 트리
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

V, E = map(int, input().split())
parent = [0] + [i for i in range(1, V+1)]
edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))
edges.sort(key=lambda x:x[2])
answer = 0
for u, v, weight in edges:
    if find(u) != find(v):
        union(u, v)
        answer += weight
print(answer)