from collections import deque
import sys
input = sys.stdin.readline

di = [-1,1,0,0] ; dj = [0,0,-1,1]
def bfs(i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    arr[i][j] = 2

    while q:
        i, j = q.popleft()


        for k in range(4):
            ni = i + di[k] ; nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] == 1:
                q.append([ni, nj])
                visited[ni][nj] = 1
                arr[ni][nj] = 2

T = int(input())    # 테스트 케이스 개수
for _ in range(T):
    N, M, K = map(int, input().split())     # N: 행 개수 / M: 열 개수 / K: 배추개수
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        arr[a][b] = 1

    cnt = 0
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                bfs(i, j)
    print(cnt)

'''
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
'''