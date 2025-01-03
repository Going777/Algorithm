import sys
from collections import deque
input = sys.stdin.readline

# 빙산의 높이는 년마다 그 칸에 동서남북 방향으로 붙어있는 0이 저장된 칸 개수만큼 준다
# 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)
# 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 0 출력

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def bfs(i, j, visited):
    visited[i][j] = 1
    q = deque([(i, j)])

    while q:
        i, j = q.popleft()

        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni, nj = i + di, j + dj

            if arr[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append([ni, nj])

def solve():
    year = 0
    while True:
        year += 1

        # [1] 네 방향의 0 개수 카운트
        arr_sub = [[0] * M for _ in range(N)]
        for i in range(1, N - 1):
            for j in range(1, M - 1):
                if arr[i][j] == 0: 
                    continue
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if arr[ni][nj] == 0:
                        arr_sub[i][j] += 1

        # [2] 높이 낮추기
        for i in range(1, N - 1):
            for j in range(1, M - 1):
                if arr_sub[i][j] > 0:
                    arr[i][j] = max(0, arr[i][j] - arr_sub[i][j])

        # [3] 빙산 개수 카운트
        visited = [[0] * M for _ in range(N)]
        cnt = 0
        for i in range(1, N - 1):
            for j in range(1, M - 1):
                if not visited[i][j] and arr[i][j] > 0:
                    bfs(i, j, visited)
                    cnt += 1
                    if cnt > 1:  # 두 덩어리 이상이면 그 시간을 리턴
                        return year
        if cnt == 0:  # 덩어리가 전부 녹았다면 0 반환
            return 0

ans = solve()
print(ans)
