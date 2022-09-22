from collections import deque
def bfs(i,j):
    q = deque()
    visited = [[0]*N for _ in range(N)]

    q.append([i,j])
    visited[i][j] = arr[i][j]

    while q:
        i, j = q.popleft()
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni = i + di ; nj = j + dj
            if 0 <= ni < N and 0 <= nj < N:
                tmp = visited[i][j] + arr[ni][nj]
                # 방문을 하지 않았거나, 현재 있는 값보다 작은 값이라면 처리
                if not visited[ni][nj] or tmp < visited[ni][nj]:
                    q.append([ni, nj])
                    visited[ni][nj] = visited[i][j] + arr[ni][nj]
    return visited[N-1][N-1]    # 맨 오른쪽 아래 값 출력

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = bfs(0,0)  # 맨 왼쪽 에서 시작
    print(f'#{tc} {ans}')

'''
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1
'''