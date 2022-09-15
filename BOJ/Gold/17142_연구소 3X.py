from collections import deque
from itertools import combinations
import copy
import sys
input = sys.stdin.readline

def bfs(lst, visited):
    q = deque()
    for i, j in lst:
        q.append([i, j])
        visited[i][j] = 1

    while q:
        i, j = q.popleft()
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni = i + di ; nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if arr[ni][nj] == 0:
                    q.append([ni, nj])
                    visited[ni][nj] = visited[i][j] + 1
                elif arr[ni][nj] == 1:
                    visited[ni][nj] = 1

    dist = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                return 0
            dist = max(dist, visited[i][j] - 1)
    return dist




N, M = map(int, input().split())    # N: 연구소 크기 / M: 바이러스 개수
# 0은 빈 칸, 1은 벽, 2는 바이러스 놓을 수 있는 위치
arr = [list(map(int, input().split())) for _ in range(N)]
virus_candidates = []
visited = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus_candidates.append([i, j])
        elif arr[i][j] == 1:
            visited[i][j] = 1

ans = N*N
for virus in combinations(virus_candidates, M):
    visited = copy.deepcopy(visited)
    tmp = bfs(virus, visited)
    if tmp == 0:
        continue
    ans = min(ans, tmp)

print(ans)