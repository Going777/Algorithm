from collections import deque

di = [-1,1,0,0] ; dj = [0,0,-1,1]
def calc_dist():
    while q:
        i, j = q.popleft()

        for k in range(4):
            ni = i + di[k] ;  nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] != 0:
                q.append([ni, nj])
                visited[ni][nj] = 1
                ans[ni][nj] = ans[i][j] + 1

N, M = map(int, input().split())    # N: 가로 수 / M: 세로 수
# 0은 갈 수 없는 땅, 1은 갈 수 있는 땅, 2는 목표지점
arr = [list(map(int, input().split())) for _ in range(N)]
ans = [[-1]*M for _ in range(N)]
q = deque()
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            q.append([i, j])
            visited[i][j] = 1
            ans[i][j] = 0
        elif arr[i][j] == 0:
            ans[i][j] = 0

calc_dist()

[print(*row) for row in ans]


'''
15 15
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
'''