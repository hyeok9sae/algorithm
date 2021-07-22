from collections import deque

def is_in(ny, nx):
    if 0 <= ny < N and 0 <= nx < N:
        return True
    return False

def flag():
    for i in range(N):
        for j in range(N):
            if nation[i][j] != 0:
                return True
    return False

def check_nation(row, col, num):
    visited[row][col] = True
    deq = deque()
    deq.append((row, col))
    sum, count = 0, 0
    flag = False
    while deq:
        y, x = deq.popleft()
        nation[y][x] = num
        sum += matrix[y][x]
        count += 1
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if not is_in(ny, nx) or nation[ny][nx] != 0 or visited[ny][nx]:
                continue
            diff = abs(matrix[y][x]-matrix[ny][nx])
            if not L <= diff <= R:
                continue
            flag = True
            visited[ny][nx] = True
            deq.append((ny, nx))
    if flag:
        calculated_people[num] = sum//count
    else:
        nation[row][col] = 0

N, L, R = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]
dy, dx = (0, -1, 0, 1), (-1, 0, 1, 0)
answer = 0
while True:
    nation = [[0]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    calculated_people = [0]*(N*N+1)
    number = 1
    for i in range(N):
        for j in range(N):
            if nation[i][j] == 0 and not visited[i][j]:
                check_nation(i, j, number)
                number += 1
    if not flag():
        break
    for i in range(N):
        for j in range(N):
            if calculated_people[nation[i][j]] == 0:
                continue
            matrix[i][j] = calculated_people[nation[i][j]]
    answer += 1
print(answer)