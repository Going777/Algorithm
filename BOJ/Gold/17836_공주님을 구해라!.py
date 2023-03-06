# (N,M) 크기
# (0,0): 출발 좌표 & (N-1, M-1): 도착 좌표 / T시간 이내로 도착해야한다
# 상하좌우 이동 가능
# 그람을 찾으면 벽 파괴 가능(개수 제한X)
# 도착 최단 시간 / T시간 이내로 도착 못한다면 'Fail' 출력

import sys
from collections import deque
input = sys.stdin.readline

def bfs(si, sj):
    global gram_dist
    visited = [[0]*M for _ in range(N)]
    q = deque()

    q.append([si, sj])
    visited[si][sj] = 1

    while q:
        i, j = q.popleft()

        # 그람 발견 => 도착지점까지 바로 갈 수 있음
        if arr[i][j] == 2:
            # 그람에서 도착지점까지의 거리 + 현재 그람까지 걸린 거리
            gram_dist = (N-1-i) + (M-1-j) + (visited[i][j]-1)

        # 도착했다면 걸린 최소시간 리턴
        if i == N-1 and j == M-1:
            return min(gram_dist, visited[i][j]-1)

        # 상하좌우 탐색
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i + di, j + dj
            # 범위 내에 존재 & 방문 X & 벽 X
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] != 1:
                q.append([ni, nj])
                visited[ni][nj] = visited[i][j] + 1

    # 도착하지 못한 경우 고려
    return gram_dist

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
gram_dist = T+1
ans = bfs(0,0)

print('Fail' if ans > T else ans)