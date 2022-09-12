# from collections import deque
# import sys
# input = sys.stdin.readline
#
# di = [-1,1,0,0,-1,1,-1,1]
# dj = [0,0,-1,1,1,1,-1,-1]
#
# def bfs(i, j):
#     q = deque()
#
#     q.append([i, j])
#     visited[i][j] = 1
#
#     while q:
#         i, j = q.popleft()
#
#         for k in range(8):
#             ni = i + di[k] ; nj = j + dj[k]
#             if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
#                 if arr[ni][nj] == 1:
#                     return visited[i][j]
#                 q.append([ni, nj])
#                 visited[ni][nj] = visited[i][j] + 1
#     return 0
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# ans = 0
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 0:
#             visited = [[0]*M for _ in range(N)]
#             tmp = bfs(i, j)
#             ans = max(ans, tmp)
# print(ans)
#
# ------------------------------------------------------------------------------

from collections import deque
import sys
input = sys.stdin.readline

di = [-1,1,0,0,-1,1,-1,1]
dj = [0,0,-1,1,1,1,-1,-1]

def bfs2():
    while q:
        i, j = q.popleft()
        for k in range(8):
            ni = i + di[k] ; nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                q.append([ni, nj])
                arr[ni][nj] = arr[i][j] + 1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append([i, j])
bfs2()
ans = 0
for row in arr:
    tmp = max(row) - 1
    ans = max(ans, tmp)
print(ans)