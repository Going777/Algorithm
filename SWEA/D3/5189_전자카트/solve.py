import sys
input = sys.stdin.readline

T = int(input())

# n은 방문한 구역 수
def dfs(n, sm, cur):
    global ans
    if n == N:
        # 여태까지의 소모량 + 1번으로 복귀비용
        ans = min(ans, sm + arr[cur][1])
        return
    
    for j in range(2, N+1):
        if not visited[j]:
            visited[j] = 1
            dfs(n+1, sm + arr[cur][j], j)
            visited[j] = 0

for t in range(1, T+1):
    N = int(input())
    arr = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    ans = 100 * N
    visited = [0] * (N+1)

    dfs(1, 0, 1)

    print(f"#{t} {ans}")