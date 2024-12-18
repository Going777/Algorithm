# from collections import deque
# di = [-1,1,0,0]; dj = [0,0,-1,1]
# def bfs(sj):
#     q = deque()

#     q.append([0,sj])
#     arr[0][sj] = 1

#     while q:
#         i, j = q.popleft()

#         if i == M-1:
#             return True

#         for k in range(4):
#             ni = i + di[k]; nj = j + dj[k]
#             if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] == 0:
#                 q.append([ni, nj])
#                 arr[ni][nj] = 1
#     return False
# M, N = map(int, input().split())    # M: 행 수 , N: 열 수
# arr = [list(map(int, input())) for _ in range(M)]
# ans = "NO"

# for j in range(N):
#     if arr[0][j] == 0:
#         if bfs(j):
#             ans = "YES"
#             break

# print(ans)


import sys
from collections import deque

# 검은색(1)-전류X, 흰색(0)-전류O
# 바깥에서 흘려 준 전류가 안쪽까지 침투될 수 있는가?
N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
result = "NO"

di=[-1,1,0,0];dj=[0,0,-1,1]
def dfs(i, j):
    global result
    visited = [[0] * M for _ in range(N)]
    visited[i][j] = 1
    q = deque([(i, j)])
    
    while q:
        i ,j = q.popleft()
        if (i == N - 1):
            result = "YES"
            break

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]

            if (0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0 and not visited[ni][nj]):
                visited[ni][nj] = 1
                q.append([ni, nj])

for j in range(M):
    if (arr[0][j] == 0):
        dfs(0, j)
        if (result == "YES"):
            break

print(result)