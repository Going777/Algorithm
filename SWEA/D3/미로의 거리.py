def bfs(si, sj):
    q = []

    q.append([si, sj])
    visited[si][sj] = 1

    while q:
        i, j = q.pop(0)
        if i == ei and j == ej:
            return visited[i][j]-2

        for di, dj in [[1,0],[-1,0],[0,-1],[0,1]]:
            ni = i + di; nj = j+dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != 1:
                q.append([ni, nj])
                visited[ni][nj] = visited[i][j] + 1

    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 출발 지점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si = i; sj = j
            elif arr[i][j] == 3:
                ei = i; ej = j

    visited = [[0]*N for _ in range(N)]
    ans = bfs(si, sj)

    print(f"#{tc} {ans}")
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