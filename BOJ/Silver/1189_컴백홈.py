def dfs(i, j, k):
    global ans
    if k > K:
        return
    if (i, j) == (ei, ej):
        if k == K:
            ans += 1
    else:
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = di + i, dj + j
            if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj] and arr[ni][nj] != 'T':
                visited[ni][nj] = 1
                dfs(ni, nj, k+1)
                visited[ni][nj] = 0


R, C, K = map(int, input().split())
arr = [list(input()) for _ in range(R)]
si, sj = R-1, 0
ei, ej = 0, C-1

ans = 0
visited = [[0]*C for _ in range(R)]
visited[si][sj] = 1
dfs(si, sj, 1)
print(ans)