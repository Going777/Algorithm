from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    q = deque()

    q.append(s)
    depth[s] += 1

    while q:
        i = q.popleft()

        for t in adjLst[i]:
            if depth[t] == -1:
                q.append(t)
                depth[t] = depth[i] + 1
                if depth[t] > K:
                    return

N, M, K, X = map(int, input().split())  # N: 도시 개수(1~N) / M: 간선개수 / K: 제한 거리 / X: 출발 도시
adjLst = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adjLst[a].append(b)

depth = [-1] * (N+1)    # 방문여부 표시 및 depth 기록을 동시에
bfs(X)

isFind = False
for i in range(N+1):
    if depth[i] == K:
        print(i)
        isFind = True

if not isFind:
    print(-1)