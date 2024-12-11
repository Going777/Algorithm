import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())
adjLst = [[] for _ in range(N + 1)]
visited = [0] * (N + 1) 
dist = [0] * (N + 1)

for _ in range(N-1):
  a, b, k = map(int, sys.stdin.readline().split())
  adjLst[a].append((b, k))
  adjLst[b].append((a, k))

def dfs(v, visited, dist):
  visited[v] = 1
  target_node = v
  max_dist = dist

  for t, k in adjLst[v]:
    if not visited[t]:
      next_node, next_dist = dfs(t, visited, dist + k)
      if (next_dist > max_dist):
        target_node, max_dist = next_node, next_dist

  return target_node, max_dist

def bfs(v, visited, dist):
  target_node = v
  max_dist = dist
  visited[v] = 1
  q = deque([(v, dist)])

  while q:
    i, d = q.popleft()

    for t, k in adjLst[i]:
      if not visited[t]:
        visited[t] = 1
        q.append([t, d + k])
        if (d + k > max_dist):
          target_node, max_dist = t, d + k

  return target_node, max_dist

# Step 1: 임의의 노드에서 가장 먼 노드 찾기
visited = [0] * (N + 1)
# target_node, _ = dfs(1, visited, 0)
target_node, _ = bfs(1, visited, 0)

# Step 2: 해당 노드에서 가장 먼 노드 찾기
visited = [0] * (N + 1)
# _, max_dist = dfs(target_node, visited, 0)
_, max_dist = bfs(target_node, visited, 0)
print(max_dist)