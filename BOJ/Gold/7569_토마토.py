from collections import deque

def bfs():
    q = deque(starts_idx)
    visited = [[[0]*M for _ in range(N)] for _ in range(H)]
    for h, i, j in starts_idx:
        visited[h][i][j] = 1

    while q:
        h, i, j = q.popleft()

        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni = i + di ; nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and arr[h][ni][nj] == 0:
                q.append([h,ni,nj])
                visited[h][ni][nj] = visited[h][i][j] + 1

M, N, H = map(int, input().split()) # M: 열 수 / N: 행 수 / H : 상자 수
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# 1은 익은 토마토, 0은 익지 않은 토마토, -1은 토마토 존재X
# 상, 하, 좌, 우, 앞, 뒤 6방향으로 퍼짐

starts_idx = []
for h in range(H):
    for i in range(N):
        for j in range(N):
            if arr[h][i][j] == 1:
                starts_idx.append([h,i,j])
bfs()