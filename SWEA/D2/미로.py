def dfs(si, sj):
    stack = []
    visited[si][sj] = 1

    while True:
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:  # 상하좌우
            ni = si + di
            nj = sj + dj
            # 상하좌우 검색, 미방문지, 갈 수 있는 길이라면(벽이 아니라면)
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != 1:
                if arr[ni][nj] == 3:    # 목적지에 도착했다면 return 1
                    return 1

                stack.append([si, sj])  # 현재 위치 기억

                si, sj = ni, nj         # 탐색 기준점 변경
                visited[si][sj] = 1     # 방문 표시
                break
        else:
            if stack:
                si, sj = stack.pop()
            else:
                break
    return 0    # 모두 탐색했지만 목적지를 발견하지 못했다면 return 0

def dfs_recur(si, sj):
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni = si + di
        nj = sj + dj
        # 상하좌우 검색, 미방문지, 갈 수 있는 길이라면(벽이 아니라면)
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != 1:
            visited[ni][nj] = 1
            dfs_recur(ni, nj)

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
    # result = dfs(si, sj)
    # print(f"#{tc} {result}")
    dfs_recur(si, sj)
    print(f"#{tc} {visited[ei][ej]}")







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