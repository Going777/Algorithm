'''
출발(맨 왼쪽 위)에서 최종 도착지(맨 오른쪽 아래)까지 지역 높이 차에 따라 연료 소비량이 달라진다
기본적으로 1만큼의 연료가 들고, 더 높은 곳으로 이동하는 경우 높이 차 만큼 추가로 연료가 추가된다
최소 연료 소비량은?
'''
from collections import deque
INF = 10000
def bfs(i, j):
    q = deque()
    visited = [[INF]*N for _ in range(N)]
    q.append([i, j])
    visited[i][j] = 0
    while q:
        i, j = q.popleft()
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N:
                tmp = visited[i][j]+1
                d_h = arr[ni][nj]-arr[i][j]
                if d_h>0:
                    tmp += d_h
                if visited[ni][nj] > tmp:
                    q.append([ni, nj])
                    visited[ni][nj] = tmp
    return visited[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = bfs(0,0)
    print(f'#{tc} {ans}')

'''
3
3
0 2 1
0 1 1
1 1 1
5
0 0 0 0 0
0 1 2 3 0
0 2 3 4 0
0 3 4 5 0
0 0 0 0 0
5
0 1 1 1 0
1 1 0 1 0
0 1 0 1 0
1 0 0 1 1
1 1 1 1 1
'''