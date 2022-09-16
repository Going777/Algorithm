from collections import deque
from itertools import combinations
import copy
import sys
input = sys.stdin.readline

def bfs(lst, visited):
    q = deque()
    for i, j in lst:
        q.append([i, j, 0])     # time(바이러스 퍼지는 시간)을 함께 넘겨줌
        visited[i][j] += 1

    while q:
        i, j, time = q.popleft()
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni = i + di ; nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == -1 and arr[ni][nj] in [0, 2]:
                q.append([ni, nj, time+1])      # 큐에 업데이트 좌표값, time+1을 넘겨줌
                if arr[ni][nj] == 2:            # 해당 위치가 비활성 바이러스 위치라면
                    visited[ni][nj] = 0         # visited에는 0 할당(카운트해주지 않기 위해)
                else:                           # 빈 칸이라면,
                    visited[ni][nj] = time+1    # visited에 지금까지의 time값 + 1 할당

    t = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:             # 방문하지 않은 곳(바이러스가 퍼지지 않은곳)이 있다면, -1 반환
                return -1
            t = max(t, visited[i][j])        # visited에서 가장 큰 값 반환
    return t

N, M = map(int, input().split())    # N: 연구소 크기 / M: 바이러스 개수
# 0은 빈 칸, 1은 벽, 2는 바이러스 놓을 수 있는 위치
arr = [list(map(int, input().split())) for _ in range(N)]
virus_candidates = []
b_visited = [[-1]*N for _ in range(N)]

cnt = 0                         # 원소값이 2(바이러스 가능 위치)와 1(벽)인 경우의 카운트 세기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:      # 바이러스 놓을 수 있는 위치인 경우, 후보군에 추가
            virus_candidates.append([i, j])
            cnt += 1
        elif arr[i][j] == 1:    # 벽인 경우 탐색할 필요 없으므로, 방문 표시
            b_visited[i][j] = 0
            cnt += 1

ans = N*N
if cnt == ans:  # 카운트가 ans와 같다면, 바이러스가 이미 모두 퍼졌거나, 퍼질 수 없는 경우 > ans = 0
    ans = 0
else:
    for virus in combinations(virus_candidates, M):
        visited = copy.deepcopy(b_visited)
        tmp = bfs(virus, visited)
        if tmp == -1:
            continue
        ans = min(ans, tmp) # 최소 시간(거리) 구하기
    if ans == N*N:          # ans값이 초기값이라면, 바이러스가 다 퍼지는 경우를 찾지 못한 것 > ans=-1
        ans = -1
print(ans)