'''
격자의 칸은 땅이거나 바다
섬은 연결된 땅이 상하좌우로 붙어있는 덩어리
다리는 바다에만 건설 가능 (다리의 길이는 격자에서 차지하는 칸의 수)
다리를 연결해서 모든 섬을 연결하려고 한다
다리의 양 끝은 섬과 인접한 바다 위에 있어야 하고, 한 다리의 방향이 중간에 바뀌면 안된다
    방향이 가로인 다리는 양 끝이 가로 방향으로 섬과 인접해야 함
    방향이 세로인 다리는 다리의 양 끝이 세로 방향으로 섬과 인접해야 함
    다리의 길이는 2 이상
모든 섬을 연결하는 다리 길이의 최솟값은? (모든 섬 연결이 불가능하면 -1)
'''
from collections import deque
di = [0,1] # 우/아래로 이동
dj = [1,0]
def bfs(i, j, k):
    q = deque()
    visited = [[0]*M for _ in range(N)]
    q.append([i, j])
    visited[i][j] = 1
    while q:
        i, j = q.popleft()
        if arr[i][j] ==1 :


        ni = i + di[k] ; nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            q.append([ni, nj])
            visited[ni][nj] = visited[i][j] + 1

N, M = map(int, input().split())
# 0은 바다, 1은 땅
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            bfs(i, j, 0)