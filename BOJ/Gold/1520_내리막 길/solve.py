import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 각 칸에는 그 지점의 높이가 쓰여있다
# 지점 사이의 이동은 상하좌우 이웃한 곳끼리만 가능
# 제일 왼쪽 위칸에서 제일 오른쪽 아래칸으로 이동하는게 목표
# 항상 높이가 더 낮은 지점으로만 이동

# 상하좌우 방향
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    # 이미 계산된 경우 바로 반환
    if dp[x][y] != -1:
        return dp[x][y]

    # 초기 경로 수는 0으로 설정
    dp[x][y] = 0

    # 상하좌우 탐색
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # 유효 범위 내에 있고 내리막길인 경우
        if 0 <= nx < N and 0 <= ny < M and arr[x][y] > arr[nx][ny]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

# 입력
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# DP 테이블: -1로 초기화 (방문하지 않음을 의미)
dp = [[-1] * M for _ in range(N)]

# 목적지에서 출발하는 경로는 1로 초기화
dp[N-1][M-1] = 1

# 시작 지점에서 dfs 탐색 시작
print(dfs(0, 0))
