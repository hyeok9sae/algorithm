# 색종이 붙이기
def is_in(ny, nx):
    if 0 <= ny < 10 and 0 <= nx < 10:
        return True
    return False

def check_cover():
    count = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 1:
                count += 1
    return count

def check(row, col, size):
    for i in range(row, row+size):
        for j in range(col, col+size):
            if not is_in(i, j):
                return False
            if matrix[i][j] == 0 or visited[i][j]:
                return False
    return True

def check_v(row, col, size, flag):
    if flag:
        color[size] -= 1
        for i in range(row, row+size):
            for j in range(col, col+size):
                visited[i][j] = True
    else:
        color[size] += 1
        for i in range(row, row+size):
            for j in range(col, col+size):
                visited[i][j] = False

def dfs(count, size):
    global result, total_one
    if result < count:
        return
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 1 and not visited[i][j]:
                break
        if matrix[i][j] == 1 and not visited[i][j]:
            break
    if matrix[i][j] == 1 and not visited[i][j]:
        for k in range(1, 6):
            if color[k] == 0:
                continue
            if check(i, j, k):
                check_v(i, j, k, True)
                total_one -= k**2
                dfs(count+1, k)
                check_v(i, j, k, False)
                total_one += k**2
            
                
    if total_one == 0:
        if result > count:
            result = count
        
matrix = [[*map(int, input().split())] for _ in range(10)]
visited = [[False]*10 for _ in range(10)]
color = [-1]+[5]*5
result = float('inf')
total_one = check_cover()
dfs(0, 0)
if result == float('inf'):
    result = -1
print(result)