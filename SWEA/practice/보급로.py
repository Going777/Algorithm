'''
출발지에서 도착지까지 가는 경로 중 복구 시간이 가장 짧은 경로에 대한 총 복구시간을 구하라
깊이가 1이라면 복구에 드는 시간은 1이다
이동 경로는 상하좌우 방향으로 한 칸씩 움직일 수 있다
현재 위치한 칸의 도로를 복구해야만 다른 곳으로 이동가능하다
출발지와 도착지를 제외한 곳이 0인 곳은 복구 작업이 필요 없는 곳
'''
from collections import deque
def bfs(i,j):
    q = deque()
    visited = [[0]*N for _ in range(N)]
    visited[i][j] = 1
    q.append([i, j])
    while q:
        i, j = q.popleft()
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni,nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:
                tmp = visited[i][j] + arr[ni][nj]
                if not visited[ni][nj] or visited[ni][nj] > tmp:
                    q.append([ni, nj])
                    visited[ni][nj] = tmp
    return visited[N-1][N-1] - 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = bfs(0,0)
    print(f'#{tc} {ans}')

'''
1
4
0100
1110
1011
1010
'''