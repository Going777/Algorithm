from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    q = deque()
    visited = [0] * (N+1)

    q.append(s)
    visited[s] += 1

    while q:
        i = q.popleft()
        if i == E:
            return visited[i] - 1
        d = [i-1, i+1]      # 탐색 리스트 만들기 (좌우 한 칸 이동한 위치)
        if adjLst[i]:       # 인접리스트 내 갈 수 있는 텔레포트가 있다면
            d += adjLst[i]  # 탐색 리스트에 해당 원소값들 추가
        for ni in d:
            if 1 <= ni <= N and not visited[ni]:
                q.append(ni)
                visited[ni] = visited[i] + 1

N, M = map(int, input().split())
S, E = map(int, input().split())
adjLst = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    adjLst[x].append(y)
    adjLst[y].append(x)

ans = bfs(S)
print(ans)