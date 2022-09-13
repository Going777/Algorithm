from collections import deque
import sys
input = sys.stdin.readline

d = [(-1,0),(1,0),(0,-1),(0,1),-1,1]
def bfs():
    q = deque(starts_idx)
    # for h, i, j in starts_idx:  # 탐색 열에 담긴 모든 곳에 방문 표시
    #     visited[h][i][j] = 1

    while q:
        h, i, j = q.popleft()

        for k in range(6):
            # 상하좌우 검사
            if k < 4:
                ni = i + d[k][0]; nj = j + d[k][1]
                if 0 <= ni < N and 0 <= nj < M and not visited[h][ni][nj]:
                    q.append([h, ni, nj])
                    visited[h][ni][nj] = visited[h][i][j] + 1
            # 박스 아래 위 검사
            else:
                nh = h + d[k]
                if 0 <= nh < H and not visited[nh][i][j]:
                    q.append([nh, i, j])
                    visited[nh][i][j] = visited[h][i][j] + 1

M, N, H = map(int, input().split()) # M: 행 수 / N: 열 수 / H : 상자 수
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# 1은 익은 토마토, 0은 익지 않은 토마토, -1은 토마토 존재X
# 상, 하, 좌, 우, 앞, 뒤 6방향으로 퍼짐

starts_idx = []
visited = [[[0]*M for _ in range(N)] for _ in range(H)]
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:           # 토마토가 있는 모든 지점 탐색 열에 추가
                starts_idx.append([h,i,j])
                visited[h][i][j] = 1        # 방문표시
            elif arr[h][i][j] == -1:        # 토마토가 들어있지 않은 곳은 탐색하지 않기 위해
                visited[h][i][j] = 1        # 방문 표시
bfs()
ans = 0
isNotMatrue = False
# 토마토 최종 상태 검사
for box in visited:
    for row in box:
        if min(row) == 0:           # 안익은 토마토가 하나라도 있으면 종료 > ans=-1
            ans = -1
            isNotMatrue = True
            break
        ans = max(ans, max(row)-1)  # 토마토 익을 때까지 걸리는 시간 구하기(visited 내 최댓값-1)
    if isNotMatrue:
        break
print(ans)