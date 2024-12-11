import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

N = 5
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

di=[-1,1,0,0]; dj=[0,0,-1,1]
def dfs(i, j, length, target_num):
  global result
  if length == 6:
      result.add(target_num)
      return
  
  for k in range(4):
    ni, nj = i + di[k], j + dj[k]
    if (0 <= ni < N and 0 <= nj < N):
        dfs(ni, nj, length + 1, target_num + str(arr[ni][nj]))
  
def bfs(i, j, length, target_num):
  global result
  q = deque([(i, j, length, target_num)])
  
  while q:
    i, j, length, target_num = q.popleft()
    if (length == 6):
      result.add(target_num)
      # continue를 하게 되면 이하 코드를 건너뛰게 됨 -> 큐에 추가 안됨 -> length > 6의 조건이 굳이 필요하지 않다
      continue 
    
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if (0 <= ni < N and 0 <= nj < N):
          q.append([ni, nj, length + 1, target_num + str(arr[ni][nj])])
        
result = set()
for i in range(N):
  for j in range(N):
    # dfs(i, j, 1, str(arr[i][j]))
    bfs(i, j, 1, str(arr[i][j]))

print(len(result))