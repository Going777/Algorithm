import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

# 사과가 1개 있는 격자(1), 장애물이 있는 격자(-1), 빈칸으로 되어 있는 격자(0)
# 상, 하, 좌, 우 방향으로 한 칸 이동
# (r,c)에서 세 번 이하의 이동으로 사과를 2개 이상 먹을 수 있으면 1, 아니면 0 출력

N = 5
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
r, c = map(int, sys.stdin.readline().split())
visited = [[0] * N for _ in range(N)]

di=[-1,1,0,0]; dj=[0,0,-1,1]
def bfs(i, j):
    # 방문 체크 및 이동 횟수 초기화
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    # 큐 초기화: (현재 행, 열, 먹은 사과 개수, 이동 횟수)
    q = deque([(i, j, arr[i][j], 0)])

    while q:
        x, y, apples, moves = q.popleft()

        # 이동 횟수가 3을 초과하면 탐색 종료
        if moves > 3:
            continue
        # 사과 2개 이상 먹으면 성공
        if apples >= 2:
            return 1

        # 4방향 탐색
        for k in range(4):
            nx, ny = x + di[k], y + dj[k]

            # 격자 범위 내, 장애물 아님, 미방문
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != -1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny, apples + arr[nx][ny], moves + 1))

    # 탐색 종료 후 조건 만족 못 하면 실패
    return 0

print(bfs(r, c))