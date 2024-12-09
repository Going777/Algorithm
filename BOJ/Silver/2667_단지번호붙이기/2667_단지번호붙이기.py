# from collections import deque

# def bfs(i, j):
#     q = deque()
#     q.append([i, j])
#     cnt = 1
#     while q:
#         i, j = q.popleft()
#         for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
#             ni, nj = di + i, dj + j
#             if 0 <= ni < N and 0<= nj < N and arr[ni][nj] == 1:
#                 arr[ni][nj] = 0
#                 q.append([ni,nj])
#                 cnt += 1
#     return cnt

# N = int(input())
# arr = [list(map(int, input())) for _ in range(N)]

# tot = 0
# cnts = []
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 1:
#             tot += 1
#             arr[i][j] = 0
#             cnts.append(bfs(i, j))

# print(tot)
# [print(x) for x in sorted(cnts)]


'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''

n = int(input())
mat = [list(map(int, input())) for _ in range(n)]
visited=[[0] * n for _ in range(n)]
cnt = 0
num_homes = []

def dfs(x, y):
  if (x < 0 or x >= n or y < 0 or y >= n or mat[x][y] == 0 or visited[x][y]):
    return 0
  
  visited[x][y] = 1

  # 현재 집(1) + 연결된 집들 재귀 탐색
  size = 1
  size += dfs(x-1, y)
  size += dfs(x+1, y)
  size += dfs(x, y-1)
  size += dfs(x, y+1)
  
  return size

for i in range(n):
  for j in range(n):
    if (mat[i][j] == 1 and not visited[i][j]):
      cnt += 1
      num_homes.append(dfs(i, j))

print(cnt)
for x in sorted(num_homes):
  print(x)