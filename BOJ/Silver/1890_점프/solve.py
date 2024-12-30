import sys
input = sys.stdin.readline

# 가장 왼쪽 위 칸에서 출발, 가장 오른쪽 아래 칸 도착
# 현재 칸에 적혀 있는 수만큼 오른쪽, 아래로만 갈 수 있다
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        target = arr[i][j]
        # 오른쪽 이동
        if (0 <= j+target < N and target > 0):
            dp[i][j+target] += dp[i][j]
        # 아래쪽 이동
        if (0 <= i+target < N and target > 0):
            dp[i+target][j] += dp[i][j]

print(dp[N-1][N-1])