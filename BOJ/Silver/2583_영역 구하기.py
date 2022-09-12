from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    q = deque()
    s = 1

    q.append([i, j])
    arr[i][j] = 1

    while q:
        i, j = q.popleft()
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni = i + di ; nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                s += 1
                q.append([ni, nj])
                arr[ni][nj] = 1
    result.append(s)

N, M, K = map(int, input().split())
arr = [[0]*M for _  in range(N)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    y1 = N - y1
    y2 = N - y2
    for i in range(y2, y1):
        for j in range(x1, x2):
            arr[i][j] = -1

cnt = 0
result = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt)
print(*sorted(result))