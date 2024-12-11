import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

# 0,0에서 출발
# 이동가능한 방향은 오른쪽과 아래
# 제일 오른쪽, 아래 칸에 도달하면 게임 승리
# 한 번에 이동할 수 있는 칸 수는, 현재 밟고 있는 칸에 쓰여 있는 수만 큼

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited=[[0] * N for _ in range(N)]
result = "Hing"

di=[0,1];dj=[1,0]
def dfs(i, j):
  global result
  if (arr[i][j] == -1):
    result = "HaruHaru"
    return 
  visited[i][j] = 1

  for k in range(2):
    weight = arr[i][j]
    ni, nj = i + (di[k] * weight), j + (dj[k] *  weight)

    if (0 <= ni < N and 0 <= nj < N and not visited[ni][nj]):
      dfs(ni, nj)

def bfs(i, j):
  global result
  visited=[[0] * N for _ in range(N)]
  visited[i][j] = 1
  q = deque([(i, j)])

  while q:
    i, j = q.popleft()
    if (i == N - 1 and j == N - 1):
      result = "HaruHaru"
      return
    
    for k in range(2):
      weight = arr[i][j]
      ni, nj = i + (di[k] * weight), j + (dj[k] * weight)
      if (0 <= ni < N and 0 <= nj < N and not visited[ni][nj]):
        visited[ni][nj] = 1
        q.append([ni, nj])
  
# dfs(0, 0)
bfs(0, 0)
print(result)