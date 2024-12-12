import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

# 1번 정점은 루트 노드
# 자식이 없는 노드는 리프 노드
# 트리의 모든 리프 노드에 게임말이 하나씩 놓인 채로 시작
# 차례가 오면 게임말을 부모 노드로 옮김(한 노드에 여러 게임말이 놓일 수 있음)
# 게임말이 루트 노드에 도착했다면 해당 게임말은 즉시 제거
# 게임말이 게임판에 존재하지 않아 고를 수 없는 사람이 패배

N = int(sys.stdin.readline())
adjLst = [[] for _ in range(N + 1)]
visited= [0] * (N + 1)
for _ in range(N - 1):
  a, b = map(int, sys.stdin.readline().split())
  adjLst[a].append(b); adjLst[b].append(a)

depth_lst = []
def dfs(v, depth):
  visited[v] = 1
  is_leaf = True

  for t in adjLst[v]:
    if not visited[t]:
      is_leaf = False
      dfs(t, depth + 1)
  
  if is_leaf:
    depth_lst.append(depth)

def bfs(v):
  q = deque([(v, 0)])
  visited = [0] * (N + 1)
  visited[v] = 1

  while q:
    i, depth = q.popleft()
    is_leaf = True

    for t in adjLst[i]:
      if not visited[t]:
        is_leaf = False
        visited[t] = 1
        q.append([t, depth + 1])
    
    if is_leaf:
      depth_lst.append(depth)


# dfs(1, 0)
bfs(1)
# 리프노드까지의 depth의 합이 홀수면 승리
print("Yes" if sum(depth_lst) % 2 else "No")
