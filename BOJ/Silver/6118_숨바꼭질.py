from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    q = deque()

    q.append(s)
    visited[s] = 1

    while q:
        i = q.popleft()
        for t in adjLst[i]:
            if not visited[t]:
                q.append((t))
                visited[t] = visited[i] + 1

N, M = map(int, input().split())
adjLst = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adjLst[a].append(b)
    adjLst[b].append(a)

visited = [0] * (N+1)
bfs(1)

visited = list(map(lambda x: x-1, visited))
mx_d = max(visited)
result = [visited.index(mx_d)]
result.append(mx_d)
result.append(visited.count(mx_d))
print(*result)