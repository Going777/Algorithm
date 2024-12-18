import sys
from collections import deque
input = sys.stdin.readline

# 빈 복도(0), 장애물(1), 딱따구리(2), 청국장(3), 스시(4), 맥앤치즈(5)
# 단위시간마다 상하좌우로 움직임
# 시작점은 딱따구리의 위치
# 가장 먼저 도착하는 음식 찾기

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
targets = {3,4,5}
def bfs(i, j):
    global cnt
    visited = [[0] * M for _ in range(N)]
    visited[i][j] = 1
    q = deque([(i, j)])
    d = [(-1,0), (1,0), (0,-1), (0,1)]
    
    while q:
        i, j = q.popleft()

        if (arr[i][j] in targets):
            cnt = visited[i][j] - 1
            return

        for (di, dj) in d:
            ni, nj = i + di, j + dj

            if (0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 1 and not visited[ni][nj]):
                visited[ni][nj] = visited[i][j] + 1
                q.append([ni, nj])

    return

cnt = 0
si, sj = 0, 0 
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2: (si, sj) = (i, j)           

bfs(si, sj)


if (cnt > 0):
    print("TAK")
    print(cnt)
else:
    print("NIE")