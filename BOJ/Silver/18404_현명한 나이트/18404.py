# 하나의 나이트 존재
# M개의 상대편 말들의 위치값이 주어진다
# 상대편 말을 잡기 위한 나이트의 최소 이동 수는?
# 8가지 위치 중 하나의 위치로 이동
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split()) # 체스판크기, 적 개수
X, Y = map(lambda x: int(x) - 1, input().split()) # 나이트의 위치
enemies = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
arr = [[0] * N for _ in range(N)]
arr[X][Y] = 1

def bfs(i, j):
    d = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]
    visited= [[0] * N for _ in range(N)]
    visited[i][j] = 1
    q = deque([(i, j)])

    while q:
        i, j = q.popleft()

        for (di, dj) in d:
            ni, nj = i + di, j + dj

            if (0 <= ni < N and 0 <= nj < N and not visited[ni][nj]):
                visited[ni][nj] = visited[i][j] + 1
                q.append([ni, nj])

    return visited

visited = bfs(X, Y)
moves= [visited[i][j] - 1 for (i, j) in enemies]

print(*moves)