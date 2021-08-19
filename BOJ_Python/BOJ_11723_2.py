# 연결 요소의 개수
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i
for _ in range(M):
    u, v = map(int, input().split())
    union(u, v)
answer = 0
for i in range(1, N+1):
    if parent[i] == i:
        answer += 1
print(answer)