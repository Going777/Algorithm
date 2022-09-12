from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    q = deque()

    q.append([i, j])
    arr[i][j] = 2
    s = 1

    while q:
        i, j = q.popleft()
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni = i + di ; nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
                q.append([ni, nj])
                arr[ni][nj] = 2
                s += 1
    return s

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
mx_s = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cnt += 1
            mx_s = max(mx_s, bfs(i, j))
print(cnt)
print(mx_s)