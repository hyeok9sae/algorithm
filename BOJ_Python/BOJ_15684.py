from itertools import product
from itertools import combinations as cb

def check():
    for i in range(1, N+1):
        res = i
        cnt = 1
        while True:
            if cnt == H+1:
                if res != i:
                    return False
                break
            # print(cnt, res)
            if matrix[cnt][res] == 0:
                cnt+=1
                continue
            else:
                res = matrix[cnt][res]
                cnt+= 1
    return True

N, M, H = map(int, input().split())
matrix = [[0]*(N+1) for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = b+1
    matrix[a][b+1] = b
lst = []
for i in product(range(1, H+1), range(1, N)):
    if matrix[i[0]][i[1]] != 0 or matrix[i[0]][i[1]+1] != 0:
        continue
    lst.append(i)
# print(lst)
cb_lst = []
flag = False
answer = 0
for i in range(4):
    cb_lst = cb(lst, i)
    for c in cb_lst:
        # print(*cb_lst, end="")
        for y, x in c:
            matrix[y][x] = x+1
            matrix[y][x+1] = x
        if check():
            flag = True
            answer = i
        for y, x in c:
            matrix[y][x] = 0
            matrix[y][x+1] = 0
        if flag:
            break
    if flag:
        break
if flag:
    print(answer)
else:
    print(-1)