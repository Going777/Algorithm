from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    q = deque()
    visited = [0] * (N+1)

    q.append(s)
    visited[s] = 1

    while q:
        i = q.popleft()
        if i == B:
            return visited[i] - 1
        for t in adjLst[i]:
            if not visited[t]:
                q.append(t)
                visited[t] = visited[i] + 1
    return -1

A, B = map(int, input().split())    # A -> B로 치환하고자 함
N, M = map(int, input().split())    # N: 전체 문자 수 / M: 치환 간으한 문자쌍의 수(간선의 수)
adjLst = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adjLst[a].append(b)
    adjLst[b].append(a)

print(bfs(A))