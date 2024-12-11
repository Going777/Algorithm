import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

N, M = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

# O : 빈 공간
# X : 벽
# I : 도연(출발 지점)
# P : 사람
di = [-1,1,0,0]; dj = [0,0,-1,1]
def dfs(i, j):
  global result
  visited[i][j] = 1

  for k in range(4):
    ni = i + di[k]
    nj = j + dj[k]
    if (0 <= ni < N and 0 <= nj < M and arr[ni][nj] != "X" and not visited[ni][nj]):
      if (arr[ni][nj] == "P"):
        result += 1
      dfs(ni, nj)

def bfs(i, j):
  global result
  _visited = [[0] * M for _ in range(N)]
  _visited[i][j] = 1
  q = deque([(i, j)])

  while q:
    i, j = q.popleft()

    for k in range(4):
      ni, nj = i + di[k], j + dj[k]
      if (0 <= ni < N and 0 <= nj < M and arr[ni][nj] != "X" and not _visited[ni][nj]):
        if (arr[ni][nj] == "P"):
          result += 1
        _visited[ni][nj] = 1
        q.append([ni, nj])

result = 0
for i in range(N):
  for j in range(M):
    if (arr[i][j] == "I"): # 도연이가 있는 곳에서 출발
      # dfs(i, j)
      bfs(i, j)

print("TT" if result == 0 else result)