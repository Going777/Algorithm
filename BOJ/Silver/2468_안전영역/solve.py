# import sys
# sys.setrecursionlimit(10 ** 6)

# N = int(sys.stdin.readline())
# arr = []
# m = 0
# for _ in range(N):
#   row = list(map(int, sys.stdin.readline().split()))
#   m = max(m, max(row))
#   arr.append(row)

# di=[-1,1,0,0]
# dj=[0,0,-1,1]
# def dfs(num, i, j, visited):
#   visited[i][j] = 1

#   for k in range(4):
#     ni = i + di[k]
#     nj = j + dj[k]
#     if (0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] > num):
#       dfs(num, ni, nj, visited)

# result = 1
# for n in range(m + 1): # n이 0일때도 고려해주어야 한다
#   visited= [[0] * N for _ in range(N)]
#   cnt = 0
#   for i in range(N):
#     for j in range(N):
#       if (not visited[i][j] and arr[i][j] > n):
#         cnt += 1
#         dfs(n, i, j, visited)
#   result = max(result, cnt)

# print(result)

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
mx = max([max(lst) for lst in arr]) # 비가 올 수 있는 최대량

def bfs(target, i, j):
    visited[i][j] = 1
    q = deque([(i, j)])

    while q:
        i, j = q.popleft()

        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i + di, j + dj

            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > target and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append([ni, nj])

ans = 0
for t in range(mx):
    tmp = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > t and not visited[i][j]:
                tmp += 1
                bfs(t, i, j)
    ans = max(ans, tmp)

print(ans)