# L은 육지 W는 바다
# 상하좌우 이웃한 육지로만 이동 가능
# 한 칸 이동하는데 한 시간 걸림
# 보물은 서로 간에 최단 거리로 이동하는 데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다
# 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안된다

from collections import deque

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(i,j):
    queue=deque()
    queue.append((i,j))
    visited=[[0]*M for _ in range(N)]
    visited[i][j]=1
    cnt=0
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            elif arr[nx][ny]=='L' and visited[nx][ny]==0:
                visited[nx][ny]=visited[x][y]+1
                cnt=max(cnt,visited[nx][ny])
                queue.append((nx,ny))
    return cnt-1

result=0
for i in range(N):
    for j in range(M):
        # 가장자리가 아님
        if i > 0 and i + 1 < N:
            if arr[i - 1][j] == "L" and arr[i + 1][j] == "L":
                continue
        if j > 0 and j + 1 < M:
            if arr[i][j - 1] == "L" and arr[i][j + 1] == "L":
                continue
        if arr[i][j]=='L':
            result=max(result, bfs(i,j))

print(result)