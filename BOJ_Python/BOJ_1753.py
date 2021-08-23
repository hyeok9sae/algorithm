# 최단경로
import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
distance = [float('inf')] * (V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
dijkstra(K)
for i in range(1, V+1):
    if distance[i] != float('inf'):
        print(distance[i])
    else:
        print("INF")