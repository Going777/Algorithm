import sys
input = sys.stdin.readline

N = int(input())
# 예외 엣지 케이스 포함하기 위해 앞,뒤로 0 추가
dp = [[0] * (12) for _ in range(101)]
dp[1][2:11] = [1] * 9

for i in range(2, 101):
    for j in range(1, 11):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

target = sum(dp[N])
print(target % 1000000000)