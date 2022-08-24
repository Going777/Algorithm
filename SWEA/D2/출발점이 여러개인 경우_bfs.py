def bfs(N):
    q = []

    # 모든 출발점 큐에 삽입
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                q.append([i, j])
                visited[i][j] =1

    while q:                            # 큐가 빌 때까지 반복
        i, j = q.pop(0)                 # 큐에서 맨 앞 원소(행위치, 열위치) 반환

        # 상하좌우 탐색
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != 1:    # 조건 만족한다면
                q.append([ni, nj])      # 큐에 위치 추가
                visited[ni][nj] = visited[i][j] + 1     # 해당 위치 방문표시
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]
    bfs(N)

    print(f"#{tc}")
    print(visited)


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