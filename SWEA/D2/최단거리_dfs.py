def dfs_recur(si, sj, s):
    global minV
    if arr[si][sj] == 3:
        s += 1
        if minV > s:
            minV = s
        return
    else:
        visited[si][sj] = 1
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni = si + di
            nj = sj + dj
            # 상하좌우 검색, 미방문지, 갈 수 있는 길이라면(벽이 아니라면)
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != 1:
                dfs_recur(ni, nj, s+1)
        visited[si][sj] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si = i; sj = j
            elif arr[i][j] == 3:
                ei = i; ej = j

    visited = [[0]*N for _ in range(N)]
    minV = N*N
    dfs_recur(si, sj, 0)
    if minV == N*N:
        minV = -1
    print(f"#{tc} {minV}")

'''
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
'''