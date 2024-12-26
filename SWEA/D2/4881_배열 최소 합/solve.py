import sys
input = sys.stdin.readline

def dfs(n, sm):
    global ans
    if ans <= sm:
        return

    if n == N:
        ans = min(ans, sm)
        return
    
    for j in range(N):
        if not visited[j]:
          visited[j] = 1
          dfs(n+1, sm + arr[n][j])
          visited[j] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 10 * N
    visited = [0] * N

    dfs(0, 0)
    print(f"#{t} {ans}")