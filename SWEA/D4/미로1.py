def bfs(si, sj):
    visited = [[0]*N for _ in range(N)]
    q = []

    q.append([si, sj])
    visited[si][sj] = 1

    while q:
        i, j = q.pop(0)
        if i == ei and j == ej:
            return 1

        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni = i + di; nj = j + dj
            if not visited[ni][nj] and arr[ni][nj] != 1:    # 방문 하지 않은 노드, 벽이 아닌 노드인 경우 큐에 추가 (사방이 벽으로 둘러있기 때문에 범위체크는 안해도됨)
                q.append([ni, nj])
                visited[ni][nj] = 1
    return 0

T = 10
for _ in range(T):
    tc = int(input())
    N = 16
    arr = [list(map(int, input())) for _ in range(16)]

    # 출발점 / 도착점 위치 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si = i; sj = j
            elif arr[i][j] == 3:
                ei = i; ej = j

    ans = bfs(si, sj)

    print(f"#{tc} {ans}")