import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
    global mx_cnt
    global result
    visited = [0]*(N+1)
    q = deque()
    cnt = 0

    q.append(s)
    visited[s] = 1

    while q:
        i = q.popleft()
        cnt += 1

        for t in adjLst[i]:
            if not visited[t]:
                q.append(t)
                visited[t] = 1

    if mx_cnt < cnt:
        mx_cnt = cnt
        result = []
        result.append(s)
    elif mx_cnt == cnt:
        result.append(s)

N, M = map(int, input().split())
adjLst = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adjLst[b].append(a)

mx_cnt = 0
result = []
for n in range(1, N+1):
    bfs(n)

print(*result)