import sys
sys.setrecursionlimit(10 ** 6)

N, M = map(int, sys.stdin.readline().split())
adjLst = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0
for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  adjLst[a].append(b)
  adjLst[b].append(a)

def dfs(v):
  visited[v] = 1

  for k in adjLst[v]:
    if not visited[k]:
      dfs(k)

for i in range(1, N+1):
  if not visited[i]:
    cnt += 1
    dfs(i)

print(cnt)
