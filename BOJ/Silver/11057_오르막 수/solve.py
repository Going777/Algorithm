import sys
input = sys.stdin.readline

N = int(input())
dp = [[0] * 10 for _ in range(1001)]
dp[1] = [1] * 10

for i in range(2, N+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:])

target = sum(dp[N])
print(target % 10007)