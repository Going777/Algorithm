# 글자인 부분은 1, 글자가 아닌 부분은 0
# 이 값을 바탕으로 1이 상,하,좌,우,대각선으로 인접하여 서로 연결되어 있다면 한 개의 글자라고 생각
# 글자의 개수는?

import sys
from collections import deque
input = sys.stdin.readline

di = [-1,1,0,0,-1,-1,1,1]
dj = [0,0,-1,1,-1,1,-1,1]

def bfs(si, sj):
    global cnt
    q = deque()
    q.append([si, sj])

    while q:
        i, j = q.popleft()
        for k in range(8):
            ni, nj = i + di[k], j + dj[k]
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and arr[ni][nj] == 1:
                q.append([ni, nj])
                visited[ni][nj] = 1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and arr[i][j] == 1:
            visited[i][j] = 1
            cnt += 1
            bfs(i, j)

print(cnt)
