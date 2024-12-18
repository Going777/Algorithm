# import sys
# from collections import deque
# sys.setrecursionlimit(10 ** 6)

# # 임의의 두 사람이 최소 몇 단계 만에 이어질 수 있는 지 계산
# # 케빈 베이컨의 수가 가장 작은 사람 = 모든 사람과 케빈 베이컨 게임을 했을 때, 나오는 단계의 합이 가장 작은 사람
# # 여러 명이라면 번호가 가장 작은 사람 출력

# N, M = map(int, sys.stdin.readline().split())
# adjLst = [[] for _ in range(N + 1)]
# visited = [0] * (N + 1)
# for _ in range(M):
#   a, b = map(int, sys.stdin.readline().split())
#   adjLst[a].append(b)
#   adjLst[b].append(a)

# def bfs(v):
#   visited = [0] * (N + 1)
#   visited[v] = 1
#   q = deque([v])
  
#   while q:
#     i = q.popleft()

#     for t in adjLst[i]:
#       if not visited[t]:
#         visited[t] = visited[i] +  1
#         q.append(t)
#   return visited

# min_num = 1
# min_depth = 10 ** 6
# for num in range(1, N + 1):
#   depth = sum(bfs(num)) - N
#   if (depth < min_depth):
#     min_num, min_depth = num, depth

# print(min_num)

'''
5 6
101010
111111
000001
111111
111111
'''

from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

di=[-1,1,0,0]; dj=[0,0,-1,1]
def bfs():
  visited = [[0] * M for _ in range(N)]
  visited[0][0] = 1
  q = deque([(0, 0)])

  while q:
    i, j = q.popleft()
    if (i == N-1 and j == N-1):
      return visited[i][j] - 1

    for k in range(4):
      ni, nj = i + di[k], j + dj[k]
    
      if (0 <= ni < N and 0 <= nj < M and arr[i][j] == 1 and not visited[ni][nj]):
        visited[ni][nj] = visited[i][j] + 1
        q.append([ni, nj])

print(bfs())