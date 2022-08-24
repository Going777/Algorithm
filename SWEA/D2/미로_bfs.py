def bfs(si, sj):
    visited = [[0]*N for _ in range(N)]
    q = []

    visited[si][sj] = 1                 # 초기 위치 방문 표시
    q.append([si, sj])                  # 초기 위치 큐에 삽입

    while q:                            # 큐가 빌 때까지 반복
        i, j = q.pop(0)                 # 큐에서 맨 앞 원소(행위치, 열위치) 반환
        if i == ei and j == ej:         # 반환된 원소가 찾는 타겟의 위치라면 타겟을 찾았으므로 종료
            return 1
        # 상하좌우 탐색
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != 1:    # 조건 만족한다면
                visited[ni][nj] = 1     # 해당 위치 방문표시
                q.append([ni, nj])      # 큐에 위치 추가
    return 0                            # 갈 수 있는 모든 정점을 돌았으나 타겟을 찾지 못한 경우

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 출발 지점, 끝 지점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
            elif arr[i][j] == 3:
                ei, ej = i, j

    result = bfs(si, sj)

    print(f"#{tc} {result}")


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