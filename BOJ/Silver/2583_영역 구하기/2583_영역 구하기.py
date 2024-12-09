# from collections import deque
# import sys
# input = sys.stdin.readline

# def bfs(i, j):
#     q = deque()
#     s = 1

#     q.append([i, j])
#     arr[i][j] = 1

#     while q:
#         i, j = q.popleft()
#         for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
#             ni = i + di ; nj = j + dj
#             if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
#                 s += 1
#                 q.append([ni, nj])
#                 arr[ni][nj] = 1
#     result.append(s)

# N, M, K = map(int, input().split())
# arr = [[0]*M for _  in range(N)]
# for _ in range(K):
#     x1, y1, x2, y2 = map(int, input().split())
#     y1 = N - y1
#     y2 = N - y2
#     for i in range(y2, y1):
#         for j in range(x1, x2):
#             arr[i][j] = -1

# cnt = 0
# result = []
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 0:
#             bfs(i, j)
#             cnt += 1
# print(cnt)
# print(*sorted(result))

import sys
sys.setrecursionlimit(10 ** 6)

M, N, K = map(int, sys.stdin.readline().split())
arr = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(M - y2, M - y1):
        for j in range(x1, x2):
            arr[i][j] = 1

visited= [[0] * N for _ in range(M)]
di=[-1,1,0,0]; dj=[0,0,-1,1]
def dfs(i, j):
  visited[i][j] = 1
  cnt = 1

  for k in range(4):
    ni = i + di[k]
    nj = j + dj[k]
    if (0 <= ni < M and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] == 0):
      cnt += dfs(ni, nj)

  return cnt

dist = 0
result = []
for i in range(M):
  for j in range(N):
    if (arr[i][j] == 0 and not visited[i][j]):
        dist += 1
        result.append(dfs(i, j))

print(dist)
print(*sorted(result))