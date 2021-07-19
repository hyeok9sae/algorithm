# 치킨 배달
from itertools import combinations as cb

def check(chick):
    answer = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                res = float('inf')
                for y, x in chick:
                    res = min(abs(y-i)+abs(x-j), res)
                answer += res
    return answer

N, M = map(int, input().split())
matrix = list(list(map(int, input().split())) for _ in range(N))
chicken = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            chicken.append((i, j))
chicken_lst = cb(chicken, M)
answer = float('inf')
for chick in chicken_lst:
    answer = min(answer, check(chick))
print(answer)