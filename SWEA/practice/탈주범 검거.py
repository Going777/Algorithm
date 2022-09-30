'''
[전형적인 테이블참조 문제]
터널 구조물 타입
    1 : 상하좌우 연결
    2 : 상하 연결
    3 : 좌우 연결
    4 : 상우 연결
    5 : 하우 연결
    6 : 하좌 연결
    7 : 상좌 연결
'''
from collections import deque
def bfs(i, j):
    global ans
    q = deque()
    q.append([i, j, arr[i][j]])
    visited[i][j] = 1
    ans += 1

    while q:
        i, j, d = q.popleft()
        if visited[i][j] == L:
            return
        for di, dj in pipe_dict[str(d)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                q.append([ni, nj, arr[ni][nj]])
                visited[ni][nj] = visited[i][j] + 1
                ans += 1


pipe_dict = {'1':[(-1,0),(1,0),(0,1),(0,-1)],
             '2':[(-1,0),(1,0)],
             '3':[(0,-1),(0,1)],
             '4':[(-1,0),(0,1)],
             '5':[(1,0),(0,1)],
             '6':[(1,0),(0,-1)],
             '7':[(-1,0),(0,-1)]}
op = []
T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())   # R/C: 맨홀 뚜겅 위치한 세로/가로 위치 / L: 탈출 후 소요시간
    arr = [list(map(int, input().strip().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not arr[i][j]:
                visited[i][j] = 1
    ans = 0
    bfs(R, C)
    print(f'#{tc} {ans}')

'''
1
5 6 2 1 3
0 0 5 3 6 0
0 0 2 0 2 0
3 3 1 3 7 0
0 0 0 0 0 0
0 0 0 0 0 0
'''