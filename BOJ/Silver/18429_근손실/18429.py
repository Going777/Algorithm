import sys
input = sys.stdin.readline

# 500이 총량
# 하루가 지날 때마다 운동을 하지 않는다면 K만큼 중량 감소
# 중량 증가량을 가지는 운동키트는 N일 동안 한 번씩만 사용 가능
# N일 동안 항상 중량이 500 이상으로 유지되도록 하는 모든 경우의 수?

N, K = map(int, input().split())
increases = list(map(int, input().split()))
visited = [0] * N
result = 0

def dfs(n, power):
    global result
    if power < 500:
        return

    if n == N:
        result += 1
        return
    
    power -= K

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(n + 1, power + increases[i])
            visited[i] = 0
    
dfs(0, 500)
print(result)